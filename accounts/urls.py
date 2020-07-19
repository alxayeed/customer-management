from django.urls import path
from .views import *


urlpatterns = [
    path('',home, name='home'),
    path('product/',product, name='product'),
    path('customer/<int:pk>/',customer, name='customer'),
]