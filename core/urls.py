from django.urls import path
from .views import initiate_payment_2, verify_payment, initiate_payment_3, verfiy_order_payment, initiate_payment_4, verify_payment2, delivery, getPrices, email_tester, delivery2


urlpatterns = [
    path("prices/", getPrices, name="get-prices"),
    path("delivery/", delivery, name="delivery"),
    path("order/<int:id>/delivery", delivery2, name="order_details_delivery"),
    path("pay/", initiate_payment_2.as_view(), name="initiate-payment"), # you changed it from initiate_payment to initiate_pay,rnt)2
    path("<int:id>/pay4/", initiate_payment_4, name="initiate-payment-4"), #This is the latest one ypu're susing"
    path("<str:ref>/", verify_payment2, name="verify-payment"), # You change this from verify_payment to verify_payment2
    path("<int:id>/verifier/", verfiy_order_payment, name="verifier"),
    path("<int:id>/pay3/", initiate_payment_3, name="initiate_payment_3"),
    path("<int:id>/email/", email_tester, name='email')
    
    
    
    
]