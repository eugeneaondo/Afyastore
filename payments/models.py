from django.db import models

# Create your models here.

class PaymentMode(models.Model):
    mode = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100)



