from django.db import models
from django.contrib.auth.models import User
import datetime 
import os 

def get_file_path(request, filename):
    original_filename = filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "%s%s" % (current_time, original_filename)
    return os.path.join('profile_pics/', filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(null=False, max_length=150)
    last_name = models.CharField(null=False, max_length=150)
    image = models.ImageField(default='defailt.jpg', upload_to= get_file_path)
    phone = models.CharField(null=False, max_length=50)
    address = models.CharField(null=False, max_length=150)
    city = models.CharField(null=False, max_length=80)
    state = models.CharField(null=False, max_length= 80)
    country = models.CharField(null=False, max_length=80)
    zip_code = models.CharField(null=False, max_length=50)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.username} Profile'
    