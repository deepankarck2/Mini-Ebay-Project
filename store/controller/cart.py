from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from store.models import Product, Cart, Bid
from django.contrib.auth.decorators import login_required
from users.models import Account
def placebid(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        if request.user.is_authenticated:
            product_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=product_id)
            if(request.POST.get('user_bid_amount')):
                user_bid_amount = int(request.POST.get('user_bid_amount'))
            else:
                return JsonResponse({'status': 'Enter a valid amount!'})
            if(product_check):
                starting_bid = product_check.bid_starting_price
                current_bid = product_check.bid_current_price
                product_quantity = int(request.POST.get('prod_quantity'))

                if(product_quantity <= 0):
                    return JsonResponse({'status': 'Given 0: Pls Add 1 or more items.'})
                elif(product_check.quantity >= product_quantity):
                    if(current_bid == None):
                        if(user_bid_amount >= starting_bid):
                            user_current_balance = request.user.account.account_balance
                            if(not user_current_balance):
                                user_current_balance = 0
                            if(user_current_balance < user_bid_amount):
                                return JsonResponse({'status': "Not Enough Money"})
                            else:
                                product_check.bid_current_price = user_bid_amount
                                product_check.save()
                                Bid.objects.create(bidder=request.user, bidding_price =user_bid_amount, product_id=product_id, quantity=product_quantity)
                                return JsonResponse({'status': "Product bid successfully!", 'reload': 'true'})
                        else:
                            return JsonResponse({'status': 'Please enter higher bid.'})
                    elif(user_bid_amount <= current_bid):
                        return JsonResponse({'status': 'Please enter higher bid.'})
                    elif(user_bid_amount > current_bid):
                        try:
                            user_current_balance = request.user.account.account_balance
                            if(not user_current_balance):
                                user_current_balance = 0
                            if(user_current_balance < user_bid_amount):
                                return JsonResponse({'status': "Not Enough Money"})
                            else:
                                bid = Bid.objects.get(bidder__id = request.user.id, product__id = product_id)
                                bid.bidder=request.user
                                bid.bidding_price =user_bid_amount
                                bid.product_id=product_id
                                bid.quantity=product_quantity
                                product_check.bid_current_price = user_bid_amount
                                product_check.save()
                                bid.save()
                            
                                return JsonResponse({'status': "Your bid has been updated!", 'reload': 'true'})
                        except Bid.DoesNotExist:
                            user_current_balance = request.user.account.account_balance
                            if(not user_current_balance):
                                user_current_balance = 0
                            if(user_current_balance < user_bid_amount):
                                return JsonResponse({'status': "Not Enough Money"})
                            else:
                                Bid.objects.create(bidder=request.user, bidding_price =user_bid_amount, product_id=product_id, quantity=product_quantity)
                                product_check.bid_current_price = user_bid_amount
                                product_check.save()
                                
                                return JsonResponse({'status': "Product bid successfully!", 'reload': 'true'})
            else:
                return JsonResponse({'status': "No such product found"})
        else:
            return JsonResponse({'status': "Login to Continue"})

    return redirect('/')


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
                    if(product_quantity <= 0):
                        return JsonResponse({'status': 'Given 0: Pls Add 1 or more items.'})
                    elif(product_check.quantity >= product_quantity):
                        Cart.objects.create(user=request.user, product_id=product_id, product_quantity=product_quantity)
                        return JsonResponse({'status': "Product added successfully"})

                    else:
                        mes = "Only " + str(product_check.quantity) + " products are available"
                        return JsonResponse({'status': mes})
            else:
                return JsonResponse({'status': "No such product found"})
        else:
            return JsonResponse({'status': "Login to Continue"})
    else:
        return redirect('store-home') 

def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user= request.user, product_id= prod_id)):
            prod_qty = int(request.POST.get('prod_quantity'))
            cart = Cart.objects.get(user= request.user, product_id = prod_id)
            cart.product_quantity = prod_qty
            cart.save()
        return JsonResponse({'status': 'sucessfully updated!'})
    else:
        return redirect('store-home')

def deleteCartItem(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user= request.user, product_id= prod_id)):
            cart = Cart.objects.get(user= request.user, product_id = prod_id)
            cart.delete()
        return JsonResponse({'status': 'sucessfully deleted!'})
    else:
        return redirect('store-home')

