from django import forms
from .models import Payment, Delivery


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["amount", "email"]



class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = "__all__"