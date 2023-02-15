from django.urls import path
from .views import initiate_payment_2, verify_payment


urlpatterns = [
    path("pay/", initiate_payment_2.as_view(), name="initiate-payment"), # you changed it from initiate_payment to initiate_pay,rnt)2
    path("<str:ref>/", verify_payment, name="verify-payment"),
]