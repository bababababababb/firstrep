from django.forms import model_to_dict
# from django.shortcuts import render
# from django.views.generic import ListView

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User, Order


class UserApi(APIView):

    def get(self, request):
        current_user_id = 300
        user_data = User.objects.get(pk=300)
        order_history = Order.objects.filter(user__id=300).values()
        return Response({
            'history': {
                'order_history': [x for x in order_history]
            },
            'user_data': model_to_dict(user_data)
        })

    def post(self, request):
        new_order = Order.objects.create(
            user_id=request.data['user_id']
        )
        return Response({'order': model_to_dict(new_order)})


# class ShopList(ListView):
#     model = User
#     template_name = 'tree/shop.html'
#     context_object_name = 'users'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = kwargs
    #     return context