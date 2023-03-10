from django.db import models
from shop.models import Product
import secrets
from django.urls import reverse
from decimal import Decimal
from coupons.models import Coupon
from django.core.validators import MinValueValidator, \
                                   MaxValueValidator
from smart_selects.db_fields import ChainedForeignKey


class LGA(models.Model):
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.city


class Delivery_prices(models.Model):
    city = models.ForeignKey(LGA, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Delivery Prices"

    def __str__(self):
        return str(self.price)

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.ForeignKey(LGA, on_delete=models.CASCADE)
    delivery_fee = ChainedForeignKey(Delivery_prices, chained_field="city",
                                     chained_model_field="city",
                                     show_all=False,
                                    auto_choose=True,
                                    sort=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    ref = models.CharField(max_length=200)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon,
                               related_name='orders',
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL)
    discount = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                       MaxValueValidator(100)])

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Order {self.id}'
    
    def get_total_cost_before_discount(self):
        return sum(item.get_cost() for item in self.items.all())
    
    def get_delivery_fee(self):
        a = self.delivery_fee
        b = str(a)
        c = float(b)
        d = int(c)
        return d

    def get_discount(self):
        total_cost = self.get_total_cost_before_discount()
        if self.discount:
            return total_cost * (self.discount / Decimal(100))
        return Decimal(0)
    

    def get_total_cost(self):
        total_cost = self.get_total_cost_before_discount() + self.get_delivery_fee()
        return total_cost - self.get_discount()
    
    def get_absolute_url(self):
        return reverse('order-details', kwargs={'id': self.pk})

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Order.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity



# YOU ADDED THIS FOR THE REFUND ON 10/02/2023
class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"





