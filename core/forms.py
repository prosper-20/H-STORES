from django import forms
from .models import Payment, Delivery, Delivery_Fee


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["amount", "email"]



class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = "__all__"

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['delivery_fee'].queryset = Delivery_Fee.objects.none()