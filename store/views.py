from django.shortcuts import render, redirect
from .models import Category, Product
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