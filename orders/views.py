from django.shortcuts import render, get_object_or_404, redirect
from .models import OrderItem
from .forms import OrderCreateForm, RefundForm
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
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order})


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,
        stylesheets=[weasyprint.CSS(
            settings.STATIC_ROOT / 'orders/pdf.css')])
    return response


# YOU JUST ADDED THIS ON THE 10/02/2023

class RequestRefundView(View):
    def get(self, *args, **kwargs):
        form = RefundForm()
        context = {
            'form': form
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
                order = Order.objects.get(ref_code=ref_code)
                order.refund_requested = True
                order.save()

                # store the refund
                refund = Refund()
                refund.order = order
                refund.reason = message
                refund.email = email
                refund.save()

                messages.info(self.request, "Your request was received.")
                return redirect("orders:request-refund")

            except ObjectDoesNotExist:
                messages.info(self.request, "This order does not exist.")
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
