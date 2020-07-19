from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'accounts/index.html')

def customer(request):
    return render(request, 'accounts/customer.html')

def product(request):
    return render(request, 'accounts/product.html')
