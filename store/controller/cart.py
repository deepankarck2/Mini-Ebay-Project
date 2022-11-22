from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from store.models import Product, Cart

def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            product_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=product_id)
        
            if(product_check):
                if(Cart.objects.filter(user=request.user.id, product_id = product_id)):
                    return JsonResponse({'status': "Product is already in cart"})
                else:
                    product_quantity = int(request.POST.get('prod_quantity'))
                    print("Pro quan: ", product_quantity)
                    if(product_check.quantity >= product_quantity):
                        Cart.objects.create(user=request.user, product_id=product_id, product_quantity=product_quantity)
                        return JsonResponse({'status': "Product added successfully"})
                    else:
                        print("HEREEEE")
                        mes = "Only " + str(product_check.quantity) + " products are available"
                        return JsonResponse({'status': mes})
            else:
                return JsonResponse({'status': "No such product found"})
        else:
            return JsonResponse({'status': "Login to Continue"})
    else:
        return redirect('store-home') 

