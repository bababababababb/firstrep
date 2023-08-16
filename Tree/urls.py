from django.urls import path

from .views import *

urlpatterns = [
    path('', ShopList.as_view(), name='home'),

]