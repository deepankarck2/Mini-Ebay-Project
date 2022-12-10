from django.urls import path
from . import views
from .controller import cart, product_modify

# Create your views here.

urlpatterns = [
    path('', views.home, name="store-home"),
    path('categories/', views.categories, name="store-categories"),
    path('categories/<str:slug>', views.categoriesview, name='categoriesview'),
    path('categories/<str:cate_slug>/<str:prod_slug>', views.product_details, name='productview'),
    path('cart/', views.viewcart, name='cart'), 

    # Add and modify Products
    path('product/add_product/', product_modify.ProductCreateView.as_view(), name="product-create"),
    path('product/<int:pk>/update_product/', product_modify.ProductUpdateView.as_view(), name="product-update"), 
    path('<int:pk>/delete_product/', product_modify.ProductDeleteView.as_view(), name="product-delete"), 
   
    path('search/', views.search, name='search'),
    path('seller-profile/<int:pk>/', views.public_seller_profile, name="public-seller-profile"),

    # Review, Rating, Report
    path('submit_review/<int:user_id>/', views.submit_review, name="submit_review"), 
    path('submit_report/<str:slug>/', views.submit_report, name="submit_report"), 

    # Buyer's Account Views
    path('buyer-account/', views.buyer_account, name="buyer_account"),
    path('buyer-account/purchase-history/', views.buyer_purchase_history, name="buyer_purchase_history"),
    path('buyer-account/bidding-history/', views.buyer_bidding_history, name="buyer_bidding_history"),

    # Seller's Account Views
    path('seller-account/', views.seller_account, name="seller_account"),
    path('manage-bids/', views.manage_bids, name="manage_bids"),
    path('manage-product-bid/<str:slug>/', views.manage_product_bid, name="manage_product_bid"),
    path('confirm-bid-sell-prod', views.confirm_bid_sell_prod, name="confirm_bid_sell_prod"),
]