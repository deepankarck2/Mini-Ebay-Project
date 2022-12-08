from django.shortcuts import render, redirect
from .models import Category, Product, Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
import json
import operator
from django.db.models import Q
import functools
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    return render(request, 'store/home.html')

def categories(request):
    category = Category.objects.filter(status=0)
    context = {
        'category' : category
    }
    return render(request, 'store/categories.html', context)

def categoriesview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context ={
            'products': products,
            'category': category
        }
        return render(request, "store/products.html", context)
    else:
        messages.warning(request, "No such Category was fouond")
        return redirect("store-collections")

def product_details(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first()
            context = {
                'products' : products,
            }
        else:
            messages(request, "No such Product found!")
            return redirect('store-collections')
    else:
        messages.error(request, "No such category found")
        return redirect('store-collections')
    
    return render(request, 'store/product_details.html', context)

@login_required
def viewcart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {
       'cart': cart
    }
    return render(request, 'store/cart.html', context)

def search(request):
    if request.GET:
        myDict = dict(request.GET)
        print(myDict)
        
        title = myDict['title[]'] if 'title[]' in myDict else None
        keyword = myDict['keyword[]'] if 'keyword[]' in myDict else None

        print(title)
        print(keyword)
        filter_prods = Product.objects.all()

        query = functools.reduce(operator.or_, (Q(name__contains = item) for item in title))
        filter_prods = filter_prods.filter(query)
        
        print(filter_prods)

        if len(keyword) > 0:
            query = functools.reduce(operator.or_, (Q(meta_keywords__contains = item) for item in keyword))
            filter_prods = filter_prods.filter(query)
        

        context = {
            'products' : filter_prods
        }
        products = render_to_string('store/filtered_prods_view.html', context)
        return JsonResponse({'data' : products})

    return render(request, 'store/search.html')

def public_seller_profile(request, pk):

    Model_one = Product.objects.filter(author__pk=pk).order_by('id')
    paginator = Paginator(Model_one, 5)
    page = request.GET.get('page1')
    try:
        Model_one = paginator.page(page)
    except PageNotAnInteger:
        Model_one = paginator.page(1)
    except EmptyPage:
        Model_one = paginator.page(paginator.num_pages)

    Model_two = Product.objects.all().order_by('id')
    paginator = Paginator(Model_two, 3)
    page = request.GET.get('page2')
    try:
        Model_two = paginator.page(page)
    except PageNotAnInteger:
        Model_two = paginator.page(1)
    except EmptyPage:
        Model_two = paginator.page(paginator.num_pages)

    context = {'model_one': Model_one, 'model_two': Model_two}

    return render(request, 'store/public_seller_profile.html', context)




# def search1(request):
#     if request.GET:
#         mydict = dict(request.GET)
#         title = mydict['title'][0]
        # if('keyword[]' in myDict):
        #     keyword = myDict['keyword[]']

        # if('title[]' in myDict):
        #     title = myDict['title[]']
#         products = Product.objects.filter(meta_keywords__contains=title)


        # if('title' in myDict):
        #     title = myDict['title']
        # elif ('title[]' or 'title' not in myDict):
        #     title = []
            

        # if('keyword' in myDict):
        #     keyword = myDict['keyword']
        # elif ('keyword[]' or 'keyword' not in myDict):
        #     keyword = []

#         print(products)
#         context = {
#          'products': products,
#         }

        # if title:
        #     filter_prods = Product.objects.filter(name__icontains=title[0])
        #     print(filter_prods)
#         return render(request, 'store/search.html', context)
#     return render(request, 'store/search.html')