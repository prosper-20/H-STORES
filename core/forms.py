from django import forms
from .models import Payment, Delivery, Delivery_Fee, Main_Delivery


class MainDeliveryForm(forms.ModelForm):
    class Meta:
        model = Main_Delivery
        fields = "__all__"


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

        if 'L_G_A' in self.data:
            try:
                lga_id = int(self.data.get('L_G_A'))
                self.fields['delivery_fee'].queryset = Delivery_Fee.objects.filter(lga_id=lga_id).order_by('lga')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['price'].queryset = self.instance.c.city_set.order_by('name')