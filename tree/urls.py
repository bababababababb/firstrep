from django.urls import path

from .views import *

urlpatterns = [
    path('api/v1/user-api', UserApi.as_view(), name='home'),

]