from django.shortcuts import render, get_object_or_404, redirect
from cart.forms import CartAddProductForm
from .models import Category, Product, Review, Contact
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib import messages
from django.views.generic import ListView
from django.db.models import Q 


def product_list2(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    total = len(products)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/store/home.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'total': total})


def product_detail2(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    reviews = Review.objects.filter(product=product)
    cart_product_form = CartAddProductForm()
    similar_products = Product.objects.filter(subcategory=product.subcategory).exclude(id=id, slug=slug) # This is to get similar products except the current one
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   "reviews": reviews,
                   "similar_products": similar_products})

def product_detail(request, id, slug):
    categories = Category.objects.all()
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    reviews = Review.objects.filter(product=product)
    cart_product_form = CartAddProductForm()
    similar_products = Product.objects.filter(subcategory=product.subcategory).exclude(id=id, slug=slug) # This is to get similar products except the current one
    return render(request,
                  'shop/store/product_detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   "reviews": reviews,
                   "categories": categories,
                   "similar_products": similar_products})



class SearchResultsView(ListView):
    model = Product
    template_name = 'shop/search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Product.objects.filter(
            Q(name__icontains=query) | Q(slug__icontains=query)
        )
        return object_list


    
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        new = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        messages.success(request, "Message received. We will get back to you shortly")
        return redirect("shop:contact")
    else:
        return render(request, "shop/contact.html")
    



class ReviewCreateView(LoginRequiredMixin, CreateView): # This is for adding a review to a product
    model = Review
    template_name = "shop/product/reviews.html"
    fields = ['body']
    success_url = "/"
    

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['id']
        form.instance.user = self.request.user
        return super().form_valid(form)