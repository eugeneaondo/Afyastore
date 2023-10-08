from django.urls import path

from . import views

urlpatterns = [
    path("all/", views.all_payments, name="all_payments")
]
