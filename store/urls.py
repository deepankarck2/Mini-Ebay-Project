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

    path('product/add_product/', product_modify.ProductCreateView.as_view(), name="product-create"),
    path('product/<int:pk>/update_product/', product_modify.ProductUpdateView.as_view(), name="product-update"), 
    path('<int:pk>/delete_product/', product_modify.ProductDeleteView.as_view(), name="product-delete"), 
    path('search/', views.search, name='search'),
    path('seller-profile/<int:pk>/', views.public_seller_profile, name="public-seller-profile"),
]