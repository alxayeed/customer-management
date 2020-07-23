from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        if self.name:
            return self.name
        else:
            return str(self.user)

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

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
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name




class Order(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Out of Stock', 'Stock Out'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer,null=True, on_delete=models.CASCADE) #Order will be deleted if the customer is deleted
    product = models.ForeignKey(Product, null=True,on_delete=models.SET_NULL) #if the Product is deleted,order will remain same with a null value for product
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)
    note = models.CharField(max_length=500, null=True)
   

    def __str__(self):
        return str(self.product)