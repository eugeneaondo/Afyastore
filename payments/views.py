from django.shortcuts import render,HttpResponse,get_object_or_404

from .models import Payment

# Create your views here.

def all_payments(request):
    payments = Payment.objects.order_by('trans_date')
    context = { "payments" : payments}
    return render(request , "payments/payments_all.html" , context)




def payment_details(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    return render(request, "payments/payment_detail.html" , {"payment" : payment})



