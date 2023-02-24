from django.contrib import admin
from .models import Payment, Order_Payment

admin.site.register(Payment)
admin.site.register(Order_Payment)
