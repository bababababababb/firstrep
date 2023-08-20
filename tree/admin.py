from django.contrib import admin

from .models import User, Book, Shop, Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'reg_date', 'id']

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'id']


admin.site.register(User, UserAdmin)
admin.site.register(Book)
admin.site.register(Shop)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)

