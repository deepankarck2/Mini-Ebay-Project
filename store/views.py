from django.shortcuts import render

def home(request):
    return render(request, 'store/home.html')

def categories(request):
    return render(request, 'store/categories.html')