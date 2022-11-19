from django.shortcuts import render
from .models import Category, Product
def home(request):
    return render(request, 'store/home.html')

def categories(request):
    category = Category.objects.filter(status=0)
    context = {
        'category' : category
    }
    return render(request, 'store/categories.html', context)