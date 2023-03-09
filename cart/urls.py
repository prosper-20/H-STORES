from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path("summary/", views.cart_detail_2, name="cart_detail_2"),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('new/add/<int:product_id>/', views.cart_add_2, name='cart_add_2'),
    path('remove/<int:product_id>/', views.cart_remove,
                                     name='cart_remove'),
]