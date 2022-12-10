"""MiniEbay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from users import views as user_views
from django.contrib.auth import views as auth_views 
from django.conf import settings
from django.conf.urls.static import static
from store.controller import cart, checkout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    
    #Users 
    path('register/', user_views.register, name='register'),  
    #path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('login/', user_views.viewLogin.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('account/', user_views.account, name='account'),

    path('add-to-cart', cart.addtocart, name="addtocart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deleteCartItem, name="deleteCartItem"),

    path('checkout', checkout.checkoutitem, name="checkout"),
    path('place-order', checkout.placeorder, name="placeorder"),

    path('place-bid', cart.placebid, name="placeBid"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)