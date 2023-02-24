from django.db import models
import secrets
from .paystack import PayStack
from orders.models import Order


class Order_Payment(models.Model):      # You just created this....
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_created"]
        verbose_name = "Ordered & Paid"
        verbose_name_plural = "Ordered & Paid"

    def __str__(self):
        return f"Payment: {self.amount}"

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)
    
    def amount_value(self):
        return self.amount * 100

    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
            if self.verified:
                return True
        return False
    

class Payment(models.Model):
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return f"Payment: {self.amount}"

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)
    
    def amount_value(self):
        return self.amount * 100

    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
            if self.verified:
                return True
        return False


class LGA(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "LGAs"
    

class Delivery_Fee(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.price}"
    
    class Meta:
        verbose_name_plural = "Delivery Fees"



class Delivery(models.Model):
    order = models.ForeignKey(Order_Payment, on_delete=models.CASCADE)
    L_G_A = models.ForeignKey(LGA, on_delete=models.CASCADE)
    delivery_fee = models.ForeignKey(Delivery_Fee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order}"
    
    class Meta:
        verbose_name_plural = "Deliveries"




# def order_payment(request, id):
#     current_order = Order.objects.get(id=id)
#     if current_order.paid == False:





