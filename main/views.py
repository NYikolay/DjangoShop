from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


class HomePage(ListView):
    model = Product
    template_name = 'main/home.html'

