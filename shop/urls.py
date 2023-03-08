from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path("shop/", views.product_list2, name="home"),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path("<int:id>/<slug:slug>/add-review", views.ReviewCreateView.as_view(), name="add-review")

]


