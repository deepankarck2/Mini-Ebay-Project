from django.db import models
from django.contrib.auth.models import User
import datetime 
import os 
from PIL import Image 

def get_file_path(request, filename):
    original_filename = filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "%s%s" % (current_time, original_filename)
    return os.path.join('profile_pics/', filename)

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(null=True,blank=True, max_length=150)
    last_name = models.CharField(null=True,blank=True, max_length=150)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to= get_file_path)
    phone = models.CharField(null=True,blank=True, max_length=50)
    address = models.CharField(null=True,blank=True, max_length=150)
    city = models.CharField(null=True,blank=True, max_length=80)
    state = models.CharField(null=True,blank=True, max_length= 80)
    country = models.CharField(null=True,blank=True, max_length=80)
    zip_code = models.CharField(null=True,blank=True, max_length=50)
    created_at = models.DateField(auto_now_add=True)
    warnings = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.user.pk} - {self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 30:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class ReviewRating(models.Model):
    review_receiver = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='for_receiver')
    review_giver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='for_giver')
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    status = models.BooleanField(default=True, help_text="True=Show, False=Don't Show")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review For- {self.review_receiver} - From {self.review_giver}'

class UserBlacklist(models.Model):
    username = models.CharField(unique=True,max_length=30) 
    email = models.CharField(unique=True,max_length=100)

    def __str__(self):
        return f'Black listed {self.username} - {self.email}' 