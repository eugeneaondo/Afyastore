from django.shortcuts import render,HttpResponse

from .models import Payment

# Create your views here.

def all_payments(request):
    Payments = Payment.objects.all()
    return HttpResponse('Here are all your payments')


def payment_details(request, payment_id):
    response = "the payment details are %s"
    return HttpResponse(response % payment_id)


