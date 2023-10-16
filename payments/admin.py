from django.contrib import admin

import afyastore

# Register your models here.


from .models import PaymentMode,Payment

admin.site.register(PaymentMode)
admin.site.register(Payment)
