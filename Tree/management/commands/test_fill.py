from django.core.management.base import BaseCommand

from Tree.models import User, Book, Shop, Order, OrderItem


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()
        Book.objects.all().delete()
        Shop.objects.all().delete()
        Order.objects.all().delete()
        OrderItem.objects.all().delete()

        users = [User(email=f'user{i}@gmail.com') for i in range(1, 101)]
        User.objects.bulk_create(users)

        books = [Book(name=f'book {i}', release_date='2022-12-12') for i in range(1, 101)]
        Book.objects.bulk_create(books)

        shops = [Shop(name=f'shop {i}') for i in range(1, 11)]
        Shop.objects.bulk_create(shops)

        orders = [Order() for i in range(50)]
        Order.objects.bulk_create(orders)

        orderitems = [OrderItem(book_quantity=i) for i in range(50)]
        OrderItem.objects.bulk_create(orderitems)

        for order in Order.objects.all():
            order.user_id = User.objects.all().order_by('?')[0]
            order.save()
        for order_item in OrderItem.objects.all():
            order_item.order_id = Order.objects.all().order_by('?')[0]
            order_item.shop_id = Shop.objects.all().order_by('?')[0]
            order_item.book_id = Book.objects.all().order_by('?')[0]
            order_item.save()
