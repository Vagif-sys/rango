from django.shortcuts import  render, get_object_or_404,redirect
from.models import *
from django.utils import timezone
from.forms import Orderform

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders':orders,'customers':customers,
    'total_orders':total_orders,'delivered':delivered,'pending':pending}

    return render(request, "rango/home.html",context)

def about(request):
    products = Product.objects.all()
    return render(request,'rango/about.html',{'products': products})

def customer(request,pk_test):
	    return render(request, 'rango/customer.html')

def creatOrder(request):
    form = Orderform()
    if request.method == 'POST':
        form = Orderform(request.POST)
        if form.is_valid():
          form.save()
          return  redirect('/')
    context = {'form':form}
    return render(request, "rango/Log.html",context)


def updateOrder(request,pk):
     order = Order.objects.get(id=pk)
     form = Orderform(instance=order)
     if request.method == 'POST':
        form = Orderform(request.POST, instance=order)
        if form.is_valid():
          form.save()
          return  redirect('/')
     context = {'form':form}
     return render(request, "rango/Log.html",context)

def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return  redirect('/')
    context = {'item':order}
    render(request, "rango/delete.html",context)
