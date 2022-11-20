from django.db import models
import datetime
import os
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
    product_image = models.ImageField( upload_to=get_file_path_pro, null=True, blank=True)
    small_description = models.TextField(max_length=250, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    bidding_price = models.FloatField(null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default= False, help_text="0=Default, 1=Hidden")
    trending = models.BooleanField(default= False, help_text="0=Default, 1=Hidden")
    tag = models.CharField(max_length=150, null=False, blank=False)
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords= models.CharField(max_length=150, null=False, blank=False)
    meta_description= models.CharField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)