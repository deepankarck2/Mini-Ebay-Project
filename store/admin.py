from django.contrib import admin
from .models import Category, Product, Cart, Order, OrderItem

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
