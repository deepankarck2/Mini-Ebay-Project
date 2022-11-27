from django.shortcuts import render, redirect
from store.models import Category, Product

from django.views.generic import CreateView


class ProductCreateView(CreateView):
    model = Product
    fields = ['category', 'name', 'slug', 'product_image', 'small_description', 'description', 'quantity', 'original_price', 'bidding_price', 'status', 'meta_title', 'meta_keywords']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)