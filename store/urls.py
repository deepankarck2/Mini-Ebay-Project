from django.urls import path
from . import views
# Create your views here.

urlpatterns = [
    path('', views.home, name="store-home"),
    path('categories/', views.categories, name="store-categories"),
]