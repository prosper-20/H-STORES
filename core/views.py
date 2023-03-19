from django.shortcuts import render, get_object_or_404, redirect
from .forms import PaymentForm, DeliveryForm, MainDeliveryForm
from django.conf import settings
from .models import Payment, Order_Payment, Delivery, Main_Delivery
from django.contrib import messages
from django.views import View
from django.views.generic import CreateView
from orders.models import Order, OrderItem
from django.http import JsonResponse
import json
from core.models import Delivery_Fee, Delivery
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse

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
    

def initiate_payment_4(request, pk):
    order = Order.objects.get(id=pk)
    orderitem = OrderItem.objects.filter(order=order)
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
        messages.success(request, f"You have successfuly paid for your order")
    else:
        messages.error(request, "Verification failed")
    return redirect("shop:product_list")

def verify_payment2(request, ref):
    order_payment = get_object_or_404(Order_Payment, ref=ref)
    current_order = order_payment.order 
    order_items = OrderItem.objects.filter(order=current_order)
    post_mail = order_payment.order.email
    verified = order_payment.verify_payment()
    if verified:
        messages.success(request, f"You have successfuly paid for your order")
        #  You just added this for the email sending
        html_template = 'core/order_on_its_way_3.html'
        my_dict = {"order_payment": order_payment,
                   "order_items": order_items}
        html_message = render_to_string(html_template, context=my_dict)
        subject = "Order Confirmation" 
        email_from = settings.EMAIL_HOST_USER
        # recipient_list = ["babatundemubaraq1650@gmail.com"]
        recipient_list = [post_mail]
        message = EmailMessage(subject, html_message,
                            email_from, recipient_list)
        message.content_subtype = "html"
        message.send()
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


def email_tester(request, id):
    order_payment = Order_Payment.objects.get(order=id)
    order_items = OrderItem.objects.filter(order=id)
    context = {
        "order_payment": order_payment,
        "order_items": order_items
    }
    return render(request, 'core/order_on_its_way_2.html', context)






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


def delivery2(request):
    form = MainDeliveryForm()
    if request.method == "POST":
        form = MainDeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Delivery info saved")
            return redirect("/")
    return render(request, "core/delivery3.html", {"form": form})


def delivery4(request, id):
    if request.method == "POST":
        address = request.POST.get("address")
        closest_stop = request.POST.get("closest_stop")
        price = request.POST.get("price")

        Main_Delivery.objects.create(order=order, address=address, closest_stop=closest_stop, price=price)
        return redirect("/")
    return render(request, "core/delivery4.html", {"order": order})

class MainDeliveryCreateView(CreateView):
    model = Main_Delivery
    fields = ['address', 'closest_stop', 'price']
    success_url = "/"

    def form_valid(self, form):
        form.instance.order = self.request.GET.get("id")
        return super().form_valid(form)





# def delivery2(request, id):
#     order_id = Order.objects.get(id=id)
#     current_order = Order_Payment.objects.get(order=order_id)
#     if request.method == "POST":
#         address = current_order.address
#         L_G_A = request.POST.get("L_G_A")
#         delivery_fee = request.POST.get("delivery_fee")
#         current_order_delivery = Delivery.objects.create(order=current_order, address=address, L_G_A=L_G_A, delivery_fee=delivery_fee)
#         context = {
#             "current_order": current_order,
#             "current_order_delivery": current_order_delivery
#             }
#         return redirect("initiate-payment-4", args=str["current_order"])
#     else:
#         return render(request, "core/delivery2.html", {"current_order": current_order})




def delivery3(request, id):
    current_order = Order.objects.get(id=id)
    if request.method == "POST":
        address = current_order.address
        L_G_A = request.POST.get("L_G_A")
        print(L_G_A)
        delivery_fee = request.POST.get("delivery_fee")
        current_order_delivery = Delivery.objects.create(order=current_order, address=address, L_G_A=L_G_A, delivery_fee=delivery_fee)
        return redirect("initiate-payment-4", kwargs={"pk": current_order})
    else:
        return render(request, "core/delivery2.html", {"current_order": current_order})






def getPrices(request):
    data = json.loads(request.body)
    lga_id = data["id"]
    print(lga_id)
    prices = Delivery_Fee.objects.filter(lga__id=lga_id)
    return JsonResponse(list(prices.values("id", "price")), safe=False)