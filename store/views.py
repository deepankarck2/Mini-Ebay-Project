from django.shortcuts import render, redirect
from .models import Category, Product, Cart, Report, Bid, Order, OrderItem, Message
from users.models import User
from users.models import ReviewRating, Account
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
import json
import operator
from django.db.models import Q
import functools
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .controller.forms import ReviewForm, ReportForm
from users.forms import UserRegisterForm, UserUpdateForm, AccountUpdateForm
import random

def home(request):
    personalized_products = Product.objects.all().order_by('?')[:5]
    print(personalized_products)
    context = {
        'personalized_products' : personalized_products
    }
    return render(request, 'store/home.html', context)

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
    paginator = Paginator(Model_one, 3)

    page = request.GET.get('page1')
    try:
        Model_one = paginator.page(page)
    except PageNotAnInteger:
        Model_one = paginator.page(1)
    except EmptyPage:
        Model_one = paginator.page(paginator.num_pages)

    all_review = ReviewRating.objects.all().order_by('id')
    Model_two = all_review.filter(review_receiver__pk = pk)
    paginator = Paginator(Model_two, 3)
    page = request.GET.get('page2')
    try:
        Model_two = paginator.page(page)
    except PageNotAnInteger:
        Model_two = paginator.page(1)
    except EmptyPage:
        Model_two = paginator.page(paginator.num_pages)

    seller = Account.objects.filter(user__id=pk).first()
    rate_count = 0
    rate_total = 0
    ave_rate = "Not Enough info"
    for review in Model_two:
        rate_count += 1
        rate_total += review.rating
    if(rate_count > 0 ):
        ave_rate = rate_total/rate_count
    else:
        ave_rate = "Not Enough review"

    context = {
        'model_one': Model_one, 
        'model_two': Model_two,
        'seller' : seller,
        'average_rate' : ave_rate
        }

    return render(request, 'store/public_seller_profile.html', context)

def submit_review(request, user_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(review_giver__id = request.user.id, review_receiver__id = user_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, "Your review has been updated!")
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.review_receiver_id = user_id
                data.review_giver_id = request.user.id
                data.save()

                messages.success(request, "Your review has been submitted!")
                return redirect(url)
    return redirect(url)


def submit_report(request, slug):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = Report()
            product = Product.objects.filter(slug=slug).first()

            report.product = product
            report.user = product.author
            report.subject = form.cleaned_data['subject']
            report.body = form.cleaned_data['body']
            report.save()
            messages.success(request, "Your Report has been submitted!")
            return redirect(url)
        else:
            messages.success(request, "Your please write a valid report!")
            return redirect(url)
    return redirect(url)

# Buyer's Account
def buyer_account(request):
    if(request.method == 'POST'):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = AccountUpdateForm(request.POST, request.FILES, instance=request.user.account)

        if(u_form.is_valid() and p_form.is_valid()):
            u_form.save()
            p_form.save()

            messages.success(request, f'Your Account has been updated')
            return redirect('account')
        else:
            messages.success(request, f'Something is Wrong!!')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = AccountUpdateForm(instance=request.user.account)
    
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'store/buyer/buyer_account.html', context)

def buyer_purchase_history(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    order_items = OrderItem.objects.filter(order__user=user)
    context = {
        "purchased_items" : order_items
    }
    return render(request, 'store/buyer/buyer_purchase_history.html', context)

def buyer_bidding_history(request):
    curr_user = request.user
    all_bids = Bid.objects.all()
    curr_user_bids = all_bids.filter(bidder_id = curr_user.id)
    context = {
        'bids' : curr_user_bids
    }
    return render(request, 'store/buyer/buyer_bidding_history.html', context)

def buyer_deposit_money(request):
    return render(request, 'store/buyer/buyer_deposit_money.html')

def confirm_deposit_money(request):
    print(request)
    if (request.method == "POST"):
        user = request.user
        deposit_amount = int(request.POST.get("deposit_amount"))
        user_obj = Account.objects.filter(user=user).first()
        user_current_banalce = user_obj.account_balance
        if(not user_current_banalce):
            user_current_banalce = 0
        user_new_balance = user_current_banalce + deposit_amount
        user_obj.account_balance = user_new_balance
        user_obj.save()
        return JsonResponse({"status" :"Deposit Successfully"})
    else:
        return JsonResponse({"status" :"Somethong went wrong"})

# Seller's Account
@login_required
def seller_account(request):
    if(request.method == 'POST'):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = AccountUpdateForm(request.POST, request.FILES, instance=request.user.account)

        if(u_form.is_valid() and p_form.is_valid()):
            u_form.save()
            p_form.save()

            messages.success(request, f'Your Account has been updated')
            return redirect('account')
        else:
            messages.success(request, f'Something is Wrong!!')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = AccountUpdateForm(instance=request.user.account)
    
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'store/seller/seller_account.html', context)

@login_required
def seller_sold_items(request):
    user = request.user
    sold_items = OrderItem.objects.filter(product__author=user)
    print(sold_items)
    context = {
        "sold_items" : sold_items
    }
    return render(request, 'store/seller/seller_sold_items.html', context)

@login_required
def manage_bids(request):
    seller_bid_products = Bid.objects.filter(product__author__id = request.user.id)
    seller_bid_products = Bid.objects.values('product').distinct()

    seller_bid_products = Product.objects.filter(id__in = seller_bid_products)

    context = {
        'seller_bid_products': seller_bid_products
    }
    return render(request, 'store/seller/manage_bids.html', context)

@login_required
def manage_product_bid(request, slug):
    seller_bid_product_items = Bid.objects.filter(product__slug = slug).order_by('-created_at')
    product = Product.objects.filter(slug=slug).first()
    context = {
        'seller_bid_product_items' : seller_bid_product_items,
        'product' : product
    }
    return render(request, 'store/seller/manage_product_bid.html', context)

@login_required
def confirm_bid_sell_prod(request):
    if request.method == 'POST':
        bid_id = request.POST.get('bid_id')
        selected_bid = Bid.objects.filter(id=bid_id).first()
        bidder = selected_bid.bidder
        product = selected_bid.product
        bidder_account = Account.objects.filter(user=bidder).first()

        newOrder = Order()
        newOrder.user = bidder
        newOrder.first_name = bidder_account.first_name
        newOrder.last_name = bidder_account.last_name
        newOrder.phone = bidder_account.phone
        newOrder.address = bidder_account.address
        newOrder.city = bidder_account.city
        newOrder.state = bidder_account.state
        newOrder.country = bidder_account.country
        newOrder.zip_code = bidder_account.zip_code

        bid_quantity = selected_bid.quantity
        selected_product_price = selected_bid.bidding_price
        bid_total_price = bid_quantity * selected_product_price

        newOrder.total_price = bid_total_price
        newOrder.status = 'Outforshipping'
        tracking_num = "Xh&y" + str(random.randint(1111111, 9999999))
        while Order.objects.filter(tracking_number = tracking_num) is None:
            tracking_num = "Xh&y" + str(random.randint(1111111, 9999999))
        newOrder.tracking_number = tracking_num
  
        newOrder.save() 
        
        bid_order_item = product
        OrderItem.objects.create(
            order = newOrder,
            product = product,
            price= selected_product_price,
            quantity = bid_quantity
        )

        #Decrease prod quantity from stock
        orderProduct = Product.objects.filter(id=product.id).first()
        orderProduct.quantity = orderProduct.quantity - bid_quantity
        orderProduct.save()

        Bid.objects.filter(product=selected_bid.product).delete()

        return JsonResponse({"status" : "Successfully Created Bid"})
    else:
        return redirect('seller_account')

@login_required
def seller_listed_items(request):
    user = request.user
    products = Product.objects.filter(author=user)
    context = {
        "products" : products
    }
    return render(request, 'store/seller/seller_listed_items.html', context)

@login_required
def seller_messages(request):
    all_messages = Message.objects.filter(user=request.user).order_by('created_at')
    paginator = Paginator(all_messages, 3)

    page = request.GET.get('page1')
    try:
        all_messages = paginator.page(page)
    except PageNotAnInteger:
        all_messages = paginator.page(1)
    except EmptyPage:
        all_messages = paginator.page(paginator.num_pages)
        
    context = {
        'all_messages' : all_messages
    }
    return render(request, 'store/seller/seller_messages.html', context)

@login_required
def admin_view(request):
    all_reports = Report.objects.all().order_by('created_at')
    paginator = Paginator(all_reports, 3)

    page = request.GET.get('page1')
    try:
        all_reports = paginator.page(page)
    except PageNotAnInteger:
        all_reports = paginator.page(1)
    except EmptyPage:
        all_reports = paginator.page(paginator.num_pages)
    context = {
        'all_reports' : all_reports
    }
    return render(request, "store/admin_view.html", context)
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