from django.urls import path

from . import views

app_name = "payments"
urlpatterns = [
    path("add_payment/", views.add_payments, name="add_payment"),
    path("all/", views.PaymentView.as_view(), name="all_payments"),
    path("<int:pk>/", views.PaymentDetailView.as_view() , name="payment_details")
]
