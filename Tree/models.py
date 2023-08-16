from django.db import models
from django.core.validators import MinValueValidator

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.email

class Book(models.Model):
    name = models.CharField(max_length=25)
    author = models.CharField(max_length=25)
    release_date = models.DateField()

class Shop(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=50)

class Order(models.Model):
    reg_date = models.DateField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    book_quantity = models.IntegerField(validators=[MinValueValidator(1, message='book_quantity can not be less than 1')])