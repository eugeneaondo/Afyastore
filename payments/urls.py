from django.urls import path

from . import views

app_name = "payments"

urlpatterns = [
    path("all/", views.all_payments, name="all_payments"),
    path("<int:payment_id>/", views.payment_details , name="payment_details")
]
