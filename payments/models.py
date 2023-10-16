from django.db import models

# Create your models here.

class PaymentMode(models.Model):
    mode = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.mode


class Payment(models.Model):
    transaction_ref = models.CharField(max_length=20, unique=True)
    mode = models.ForeignKey(PaymentMode ,on_delete=models.CASCADE )
    amount = models.DecimalField(max_digits=12,decimal_places=2 )
    paid_by = models.CharField(max_length=30)
    trans_date = models.DateTimeField("Trancation Date")

    def __str__(self):
        return self.transaction_ref + " amount is " + str(self.amount) + " " + str(self.trans_date)




