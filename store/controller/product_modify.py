from django.shortcuts import render, redirect
from store.models import Category, Product

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['category', 'name', 'slug', 'product_image', 'small_description', 'description', 'quantity', 'original_price', 'bidding_price', 'status', 'meta_title', 'meta_keywords']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['category', 'name', 'slug', 'product_image', 'small_description', 'description', 'quantity', 'original_price', 'bidding_price', 'status', 'meta_title', 'meta_keywords']
    pk_url_kwarg = 'pk'
    query_pk_and_slug = True
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            False

class ProductDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            False
    