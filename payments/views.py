from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,HttpResponse,get_object_or_404
from django.views import generic
from .models import Payment,PaymentMode
from customers.models import Customer

# Create your views here.

def add_payments(request):
    payment_mode = PaymentMode.objects.all()
    customers = Customer.objects.all()
    context = { "payment_mode" : payment_mode , "customers" : customers }
    return render(request, "payments/add_payment.html", context )


class PaymentView(generic.ListView):
    template_name = "payments/payments_all.html"
    context_object_name = "payments"

    def get_queryset(self) -> QuerySet[Any]:
        return Payment.objects.order_by('trans_date')

class PaymentDetailView(generic.DetailView):
    model = Payment
    template = "payments/payment_detail.html"


    
    
#previous code 

""" def all_payments(request):
    payments = Payment.objects.order_by('trans_date')
    context = { "payments" : payments}
    return render(request , "payments/payments_all.html" , context)
 """



""" def payment_details(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    return render(request, "payments/payment_detail.html" , {"payment" : payment}) """





