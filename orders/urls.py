from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'), # ypu bchanged this from 'views.order_create' to views.order_create_2
    path('admin/order/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
    path('admin/order/<int:order_id>/pdf/', views.admin_order_pdf, name='admin_order_pdf'),
    path('request-refund/', views.RequestRefundView.as_view(), name='request-refund'),
    path("history/", views.history, name="history"),
    path("orders/history/", views.order_history, name="order-history")
]
