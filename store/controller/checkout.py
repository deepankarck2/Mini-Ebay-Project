from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from store.models import Cart 

@login_required
def checkoutitem(request):
    rawcart = Cart.objects.filter(user = request.user)
    for item in rawcart:
        if item.product_quantity >  item.product.quantity:
            Cart.objects.delete(id = item.id)
        else: 
            pass 
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0

    for item in cartitems:
        total_price = total_price + item.product_quantity * item.product.original_price
    
    context = {
        'cartitems' : cartitems,
        'total_price': total_price,
    } 

    return render(request, "store/checkout.html", context)