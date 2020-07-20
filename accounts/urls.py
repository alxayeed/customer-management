from django.urls import path
from .views import *


urlpatterns = [
    path('',home, name='home'),
    path('product/',product, name='product'),
    path('customer/<int:pk>/', customer, name='customer'),
    path('create-order/<int:pk>/',createOrder, name="create_order"),
    path('update-order/<int:pk>/',updateOrder, name="update_order"),
    path('delete-order/<int:pk>/',deleteOrder, name="delete_order"),
]