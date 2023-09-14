from django.shortcuts import render, HttpResponse

# Create your views here.


def customers(request):
    return HttpResponse("hello to all of our customers")