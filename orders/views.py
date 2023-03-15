from django.shortcuts import render, get_object_or_404, redirect
from .models import OrderItem, Order
from .forms import OrderCreateForm, RefundForm, OrderSummaryAndEditForm
from .tasks import order_created
from cart.cart import Cart
from django.contrib.admin.views.decorators import staff_member_required
from .models import Order, Refund
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from django.conf import settings
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.models import Order_Payment
from core.models import Order_Payment
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from shop.models import Product, Category
from django.contrib.auth.decorators import login_required

@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            order_created.delay(order.id)
            first_name = form.cleaned_data["first_name"]
            messages.warning(request, "Disclaimer: Pls do not reload this page")
            return render(request,
                          'orders/order/created.html',
                          {'order': order,
                          'first_name': first_name})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})

# This is a test order_create form

def order_create_2(request):
    cart = Cart(request)
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        postal_code = request.POST.get("postal_code")
        city = request.POST.get("city")

        order = Order.objects.create(first_name=first_name, last_name=last_name,
        email=email, address=address, postal_code=postal_code, city=city)
        order.save()
        if cart.coupon:
            order.coupon = cart.coupon
            order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            order_created.delay(order.id)
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/new_create.html',
                  {'cart': cart, 'form': form})




        


@staff_member_required
def admin_order_detail(request, order_id):
    # order_payment = get_object_or_404(Order_Payment, id=order_id) # You changed this from get_object_or_404(Order, id=order_id) to what you have
    order_payment = Order_Payment.objects.get(id=order_id)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order_payment': order_payment})


@staff_member_required
def admin_order_pdf(request, order_id):
    order_payment = get_object_or_404(Order_Payment, id=order_id) # You changed this from get_object_or_404(Order, id=order_id) to what you have
    html = render_to_string('orders/order/pdf.html',
                            {'order_payment': order_payment})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order_payment.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,
        stylesheets=[weasyprint.CSS(
            settings.STATIC_ROOT / 'orders/pdf.css')])
    return response


# YOU JUST ADDED THIS ON THE 10/02/2023

class RequestRefundView(View):
    def get(self, *args, **kwargs):
        form = RefundForm()
        context = {
            'form': form,
            'title': 'Request Refund'

        }
        return render(self.request, "orders/order/request_refund.html", context)

    def post(self, *args, **kwargs):
        form = RefundForm(self.request.POST)
        if form.is_valid():
            ref_code = form.cleaned_data.get('ref_code')
            message = form.cleaned_data.get('message')
            email = form.cleaned_data.get('email')
            # edit the order
            try:
                order = Order.objects.get(ref=ref_code)
                order.refund_requested = True
                order.save()

                # store the refund
                refund = Refund()
                refund.order = order
                refund.reason = message
                refund.email = email
                refund.save()

                messages.info(self.request, "Your request was received.  An agent will get back to you within an hour. Thank you!")
                return redirect("shop:product_list")

            except ObjectDoesNotExist:
                messages.info(self.request, "This order does not exist, Kindly check the order details")
                return redirect("orders:request-refund")


# YOU JUST ADDED THIS ON THE 10/02/2023
@login_required
def history(request):
    completed_orders = Order.objects.filter(email=request.user.email, paid=True)
    incomplete_orders = Order.objects.filter(email=request.user.email, paid=False)

    context = {
        "incomplete_orders": incomplete_orders,
        "completed_orders": completed_orders
    }
    return render(request, "orders/order/history.html", context)


# Order detail view for the user
def user_order_detail(request, order_id):
    order_payment = get_object_or_404(Order_Payment, id=order_id) # You changed this from get_object_or_404(Order, id=order_id) to what you have
    return render(request,
                  'admin/orders/order/user_detail2.html', # You changed this from user_detail.html to user_detail2.html
                  {'order_payment': order_payment})

@login_required
def order_history(request):
    completed_orders = Order_Payment.objects.filter(email=request.user.email, verified=True)
    incomplete_orders = Order.objects.filter(email=request.user.email, paid=False)

    context = {
        "incomplete_orders": incomplete_orders,
        "completed_orders": completed_orders
    }
    return render(request, "orders/order/history2.html", context)



def pay_later(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    messages.success(request, f"Your order has been saved. Kindly check your hisory to view your order")
    context = {'category': category,
                   'categories': categories,
                   'products': products}
    return render(request, 'shop/product/list.html', context)


def order_summary(request, id):
    current_order = Order.objects.get(id=id)
    current_orderitem = OrderItem.objects.get(order=id)
    context = {
        "current_orderitem": current_orderitem,
        "current_order": current_order
    }
    return render(request, "orders/order/order_summary.html", context)


def order_details(request, id):
    current_order = Order.objects.get(id=id)
    current_orderitem = OrderItem.objects.filter(order=current_order)

    context = {
        "current_order": current_order,
        "current_orderitem": current_orderitem,
        "title": "Order | Details"
    }
    return render(request, "orders/order/order_details.html", context)







# def order_summary_and_edit(request, id):
#     if request.method == "POST":
#         order_form = OrderSummaryAndEditForm(request.POST,
#                                    request.FILES,
#                                    instance=request.id)
#         if order_form.is_valid():
#             order_form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('profile')

#     else:
#          order_form = OrderSummaryAndEditForm(instance=request.id)

#     context = {
#         'order_form': order_form
#     }

#     return render(request, 'orders/order/order_summary_edit.html', context)

class OrderItemUpdateView(LoginRequiredMixin, UpdateView):
    model = OrderItem
    fields = ['product', 'quantity']
    template_name = "orders/order/order_form_2.html"


class OrderSummaryUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'address',
                  'postal_code', 'city']
    
    

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False





