from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name

class Product(models.Model):
    CATAGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Out door')
    )
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    catagory = models.CharField(max_length=100, choices=CATAGORY, null=True)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)


class Order(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Out of Stock', 'Stock Out'),
        ('Delivered', 'Delivered'),
    )
    # customer = models.ForeignKey(Customer, on_delete=CASCADE)
    # product = models.ForeignKey(Product, on_delete=CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)