from django.shortcuts import render,HttpResponse, get_object_or_404
from django.http import  HttpResponseRedirect
from .models import Product, Order, OrderItem
from django.urls import reverse
# Create your views here.

def index(request):
    return HttpResponse("index for ordermanagement")
#products mgmt
def product_list(request):
    products = Product.objects.all()
    return render(request, 'ordermanagement/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'ordermanagement/product_detail.html', {'product': product})

#orders
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'ordermanagement/order_detail.html', {'order': order})


