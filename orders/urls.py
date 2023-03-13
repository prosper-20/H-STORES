from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'), # ypu bchanged this from 'views.order_create' to views.order_create_2
    path("<int:id>/details/", views.order_details, name='order-details'),
    path("<int:pk>/summary/edit/", views.OrderSummaryUpdateView.as_view(), name='order-summary-edit'),
    path("<int:id>/summary/", views.order_summary, name="order-summary"),
    path("<int:pk>/items/edit", views.OrderItemUpdateView.as_view(), name="orderitem-edit"),
    path('admin/order/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
    path('user/order/<int:order_id>/', views.user_order_detail, name='user-order-detail'),
    path('admin/order/<int:order_id>/pdf/', views.admin_order_pdf, name='admin_order_pdf'),
    path('request-refund/', views.RequestRefundView.as_view(), name='request-refund'),
    path("history/", views.history, name="history"),
    path("orders/history/", views.order_history, name="order-history"),
    path("pay-later/", views.pay_later, name="pay-later")
]


