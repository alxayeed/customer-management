from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from .models import *
from .forms import *

# Create your views here.


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders , 'delivered': delivered, 'pending' : pending}
    
    return render(request, 'accounts/index.html', context)

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()

    total_order = customer.order_set.all().count()

    context = {'customer': customer, 'orders': orders, 'total_order': total_order }
    return render(request, 'accounts/customer.html', context)

def product(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'accounts/product.html', context)


def createOrder(request, pk):
    OrderFromSet = inlineformset_factory(Customer, Order, fields=('product', 'status'))
    customer = Customer.objects.get(id=pk)
    formset = OrderFromSet(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer':customer})
    if request.method == "POST":
        # form = OrderForm(request.POST)
        formset = OrderFromSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()

            return redirect('/')

    context = {'formset': formset}

    return render(request, 'accounts/order_form.html', context)
    

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    context = {'form': form}
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    context = {'order': order}
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    return render(request, 'accounts/delete.html', context)
