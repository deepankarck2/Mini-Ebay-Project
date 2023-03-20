from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from store.models import Cart, Order, OrderItem, Product
from users.models import Account
import random

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

@login_required
def placeorder(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.original_price * item.product_quantity
        user = request.user
        user_current_balance = user.account.account_balance
        if(not user_current_balance):
            user_current_balance = 0
        if(user_current_balance < cart_total_price):
            messages.success(request, "Not Enough Money")
        else:
            newOrder = Order()
            newOrder.user = user
            newOrder.first_name = request.POST.get('ck_first_name')
            newOrder.last_name = request.POST.get('ck_last_name')
            newOrder.phone = request.POST.get('ck_phone')
            newOrder.address = request.POST.get('ck_address')
            newOrder.city = request.POST.get('ck_city')
            newOrder.state = request.POST.get('ck_state')
            newOrder.country = request.POST.get('ck_country')
            newOrder.zip_code = request.POST.get('ck_ck_zip')
            newOrder.city = request.POST.get('ck_city')

            newOrder.total_price = cart_total_price
            tracking_num = "Xh&y" + str(random.randint(1111111, 9999999))
            while Order.objects.filter(tracking_number = tracking_num) is None:
                tracking_num = "Xh&y" + str(random.randint(1111111, 9999999))
            newOrder.tracking_number = tracking_num
            buyer_user_account = Account.objects.filter(user = user).first()

            buyer_user_account.account_balance = user_current_balance - cart_total_price
            buyer_user_account.save()
            newOrder.save() 

            newOrderItems = Cart.objects.filter(user=request.user)
            for item in newOrderItems:
                OrderItem.objects.create(
                    order = newOrder,
                    product = item.product,
                    price= item.product.original_price,
                    quantity = item.product_quantity
                )
                #Decrease prod quantity from stock
                orderProduct = Product.objects.filter(id=item.product_id).first()
                orderProduct.quantity = orderProduct.quantity - item.product_quantity
                orderProduct.save()
        
            ## To clear User Cart
            Cart.objects.filter(user=request.user).delete()

            messages.success(request, "Your Order has been placed successfully")
    return redirect(url)

