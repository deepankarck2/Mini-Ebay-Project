from django.db import models
from django.contrib.auth.models import User
import datetime
import os
from django.urls import reverse

# Create your models here.

def get_file_path_cat(request, filename):
    original_filename = filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "%s%s" % (current_time, original_filename)
    return os.path.join('uploads_category/', filename)

def get_file_path_pro(request, filename):
    original_filename = filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "%s%s" % (current_time, original_filename)
    return os.path.join('uploads_product/', filename)

class Category(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField( upload_to=get_file_path_cat, null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default= False, help_text="0=Default, 1=Hidden")
    trending = models.BooleanField(default= False, help_text="0=Default, 1=Hidden")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords= models.CharField(max_length=150, null=False, blank=False)
    meta_description= models.CharField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path_pro, null=True, blank=True)
    small_description = models.TextField(max_length=250, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    bid_starting_price = models.FloatField(null=False, blank=False)
    bid_current_price = models.FloatField(null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default= False, help_text="0=Show, 1=Hidden")
    bid_status = models.BooleanField(default= False, help_text="0=Show, 1=Hidden")
    trending = models.BooleanField(default= False, help_text="0=Default, 1=Hidden")
    tag = models.CharField(max_length=150, null=False, blank=False)
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords= models.CharField(max_length=150, null=False, blank=False)
    meta_description= models.CharField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
        
    def get_absolute_url(self):
        return reverse('productview', kwargs={"cate_slug": self.category.slug, "prod_slug": self.slug})
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.IntegerField(null=False, blank=False)
    created_at = models.DateField( auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    first_name = models.CharField(null=True,blank=True, max_length=150)
    last_name = models.CharField(null=True,blank=True, max_length=150)
    phone = models.CharField(null=True,blank=True, max_length=50)
    address = models.CharField(null=True,blank=True, max_length=150)
    city = models.CharField(null=True,blank=True, max_length=80)
    state = models.CharField(null=True,blank=True, max_length= 80)
    country = models.CharField(null=True,blank=True, max_length=80)
    zip_code = models.CharField(null=True,blank=True, max_length=50)
    total_price = models.FloatField(null=False)
    payment_id = models.CharField(max_length=150, null=True)
    orderStatuses = (
        ('Pending', "Pending"),
        ('Outforshipping', 'Out for Shipping'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(max_length=150, choices=orderStatuses, default='Pending')
    message = models.TextField(null=True)
    tracking_number = models.CharField(max_length=150, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.tracking_number}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.order.id} - {self.product.slug}'

class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bidding_price = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    orderStatuses = (
        ('Pending', "Pending"),
        ('Bid_Accepted', 'Bid_Accepted'),
        ('Bid_Rejected', 'Bid_Rejected'),
    )
    bid_status = models.CharField(max_length=150, choices=orderStatuses, default='Pending')
    quantity = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now=True)

class Report(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Product Owner", on_delete=models.CASCADE)
    subject = models.CharField(max_length=150, help_text="Suject of the report", blank=False)
    body = models.TextField(max_length=500, blank=True, null=True)
