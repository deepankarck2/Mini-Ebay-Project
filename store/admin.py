from django.contrib import admin
from .models import Category, Product, Cart, Order, OrderItem, Bid, Report

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)

class BidAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
admin.site.register(Bid, BidAdmin)

admin.site.register(Report)
