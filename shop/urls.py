from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path("shop/", views.product_list2, name="home"), 
    path("contact/", views.contact, name="contact"),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path("new/<int:id>/<slug:slug>/", views.product_detail2, name="product_detail_2"),
    path("<int:id>/<slug:slug>/add-review", views.ReviewCreateView.as_view(), name="add-review")

]


