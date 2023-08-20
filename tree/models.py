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
    author = models.CharField(max_length=50)
    release_date = models.DateField()

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Order(models.Model):
    reg_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.email

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)
    book_quantity = models.IntegerField(validators=[MinValueValidator(1, message='book_quantity can not be less than 1')])

    def __str__(self):
        return str(self.book_quantity)