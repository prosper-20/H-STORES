from django.shortcuts import render, get_object_or_404, redirect
from .forms import PaymentForm
from django.conf import settings
from .models import Payment
from django.contrib import messages
from django.views import View

def initiate_payment(request):
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            # return render(request, "core/make_payment.html", {"payment": payment, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
            # return render(request, "core/make_payment_2.html", {"payment": payment, 'paystack_public_key': 'pk_test_db7eb580c0015ee09205de7791906de5b11d108d'})
            return render(request, "core/make_payment.html", {"payment": payment, 'paystack_public_key': 'pk_test_db7eb580c0015ee09205de7791906de5b11d108d'})
        
    else:
        payment_form = PaymentForm()
    return render(request, "core/initiate_payment_2.html", {"payment_form": payment_form})




class initiate_payment_2(View):
    def get(request):
        payment_form = PaymentForm()
        return render(request, "core/initiate_payment_2.html", {"payment_form": payment_form})


    def post(request):
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(request, "core/make_payment.html", {"payment": payment, 'paystack_public_key': 'pk_test_db7eb580c0015ee09205de7791906de5b11d108d'})




# def initiate_payment_2(request):
#     if request.method == "POST":
#         amount = request.POST.get("amount")
#         email = request.POST.get_enail
#         payment_form = Payment.objects.create(amount=amount, email=email)
#         payment_form.save()
#         return render(request, "core/make_payment_2.html")
#     else:




def verify_payment(request, ref):
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, "Verification successful")
    else:
        messages.error(request, "Verification failed")
    return redirect("initiate-payment")
