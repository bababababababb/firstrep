from django.contrib import admin

from .models import User, Book, Shop, Order, OrderItem

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Shop)
admin.site.register(Order)
admin.site.register(OrderItem)