from django.shortcuts import render, get_object_or_404, redirect
from .forms import PaymentForm, DeliveryForm
from django.conf import settings
from .models import Payment, Order_Payment
from django.contrib import messages
from django.views import View
from django.views.generic import CreateView
from orders.models import Order, OrderItem
from django.http import JsonResponse

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
    def get(self, request):
        payment_form = PaymentForm()
        return render(request, "core/initiate_payment_2.html", {"payment_form": payment_form})


    def post(self, request):
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(request, "core/make_payment.html", {"payment": payment, 'paystack_public_key': 'pk_test_db7eb580c0015ee09205de7791906de5b11d108d'})


def initiate_payment_3(request, id):
    order = Order.objects.get(id=id)
    if request.method == "POST":
        amount = order.get_total_cost()
        email = order.email

        payment = Payment.objects.create(amount=amount, email=email)
        context = {
            "payment": payment, 
            'order': order,
            'paystack_public_key': 'pk_test_db7eb580c0015ee09205de7791906de5b11d108d'
        }
        return render(request, "core/make_payment.html", context)
    
    else:
        context = {
            'order': order,
        }
        return render(request, "core/initiate_payment_3.html", context)
    

def initiate_payment_4(request, id):
    order = Order.objects.get(id=id)
    orderitem = OrderItem.objects.get(order=order)
    if request.method == "POST":
        amount = order.get_total_cost()
        email = order.email

        order_payment = Order_Payment.objects.create(order=order, amount=amount, email=email)
        context = {
            "order_payment": order_payment, 
            'order': order,
            "orderitem": orderitem,
            'paystack_public_key': 'pk_test_db7eb580c0015ee09205de7791906de5b11d108d'
        }
        return render(request, "core/make_payment4.html", context) # You changed it from make_payment to make_payment4
    
    else:
        context = {
            'order': order,
            "orderitem": orderitem,
        }
        return render(request, "core/initiate_payment_4.html", context)




# class PaymentCreateView(CreateView):
#     model = Payment
#     template_name = "class_create.html"
#     fields = ["email"]
#     success_url = "/"

#     def form_valid(self, form):
#         form.instance.


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
        messages.success(request, f"Verification successful")
    else:
        messages.error(request, "Verification failed")
    return redirect("shop:product_list")

def verify_payment2(request, ref):
    order_payment = get_object_or_404(Order_Payment, ref=ref)
    verified = order_payment.verify_payment()
    if verified:
        messages.success(request, f"Verification successful")
    else:
        messages.error(request, "Verification failed")
    return redirect("shop:product_list")



# def verify_payment_2(request, ref, id):
#     payment = get_object_or_404(Payment, ref=ref)
#     order = get_object_or_404(Order, id=id)
#     verified = payment.verify_payment()
#     if verified:
#         messages.success(request, f"Verification successful")
#     else:
#         messages.error(request, "Verification failed")
#     return redirect("shop:product_list")






def verfiy_order_payment(request, id): # This is to change the  order.paid to True
    order = Order.objects.get(id=id)
    payment = Payment.objects.filter(amount=order.get_total_cost(),
                                     email=order.email, verified=True)
    if payment.exists():
        order.paid = True
        order.save()
        messages.success(request, "Payment has been made for your order")
        return redirect("/")
    else:
        messages.error(request, "No matching order found")
        return redirect("/")



# class PaymentCreateView(CreateView):
#     model = Payment
#     success_url = "/"
#     fields = ["email"]

#     def form_valid(self, form):
#         form.instance.amount = self.request.order.get_total_cost
#         return super().form_valid(form)




# def payment_order(request, id):
#     current_order = Order.objects.get(id=id)
#     if current_order.paid == False:
#         order_email = current_order.email
#         order_amount = current_order.get_total_cost()
#         if Payment.objects.filter(amount=order_amount, email=order_email):



def delivery(request):
    form = DeliveryForm()
    if request.method == "POST":
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "core/delivery.html", {"form": form})



def getPrices(request):
    return JsonResponse("It is working", safe=False )