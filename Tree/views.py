from django.shortcuts import render
from django.views.generic import ListView

from .models import *

class ShopList(ListView):
    model = User
    template_name = 'Tree/shop.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = kwargs
        return context