from django.shortcuts import render, redirect
from .models import Category, Product, Cart
from django.contrib import messages

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

def viewcart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {
       'cart': cart
    }
    return render(request, 'store/cart.html', context)