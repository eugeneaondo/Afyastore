from django.shortcuts import render,HttpResponse

# Create your views here.

def all_payments(request):
    return HttpResponse('Here are all your payments')


