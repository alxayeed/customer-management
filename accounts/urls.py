from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('signup/',createUser, name='signup'),
    path('login/',loginUser, name='login'),
    path('logout/',logoutUser, name='logout'),
    path('account/',acountSettings, name='account'),
    path('product/',product, name='product'),
    path('user/',userHome, name='user_home'),
    path('customer/<int:pk>/', customer, name='customer'),
    path('create-order/<str:pk>/',createOrder, name="create_order"),
    path('update-order/<int:pk>/',updateOrder, name="update_order"),
    path('delete-order/<int:pk>/',deleteOrder, name="delete_order"),
    path('reset-password/',
    auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
    name='reset_password'),

    path('reset-password-sent/',
    auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset_password_sent.html'),
    name='password_reset_done'),

    path('reset-password/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(),
    name='password_reset_confirm'),
     
    path('reset-password-complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_complete.html'),
     name='password_reset_complete'),
]