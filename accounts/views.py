from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import connection
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from .filters import OrderFilter

# Create your views here.


@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders , 'delivered': delivered, 'pending' : pending}
    
    return render(request, 'accounts/index.html', context)

def createUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account Succesfully Created for {username}')
                return redirect('login')
        
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # with connection.cursor() as cursor:
                #     cursor.execute("SELECT id FROM User Where username= %s",[username])
                #     pk = cursor.fetchone()
                    login(request, user)
                    return redirect('home')

            else:
                messages.info(request,'Username or Password is incorrect')

        return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()

    total_order = customer.order_set.all().count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer': customer, 'orders': orders, 'total_order': total_order, 'myFilter': myFilter }
    return render(request, 'accounts/customer.html', context)

@login_required(login_url='login')
def product(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'accounts/product.html', context)

@login_required(login_url='login')
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
    
@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    context = {'order': order}
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    return render(request, 'accounts/delete.html', context)
