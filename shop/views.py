from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product, Review
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView


def product_list(request, category_slug=None):
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


def product_detail(request, id, slug):
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



class ReviewCreateView(LoginRequiredMixin, CreateView): # This is for adding a review to a product
    model = Review
    template_name = "shop/product/reviews.html"
    fields = ['body']
    success_url = "/"

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['id']
        form.instance.user = self.request.user
        return super().form_valid(form)