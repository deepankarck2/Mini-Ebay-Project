from django.urls import path
from . import views
from .controller import cart
# Create your views here.

urlpatterns = [
    path('', views.home, name="store-home"),
    path('categories/', views.categories, name="store-categories"),
    path('categories/<str:slug>', views.categoriesview, name='categoriesview'),
    path('categories/<str:cate_slug>/<str:prod_slug>', views.product_details, name='productview'),
    path('cart/', views.viewcart, name='cart'), 
]