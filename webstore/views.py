from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product
from basket.forms import BasketAddProductForm

def product_list(request, category_slug = None):
    templates = 'webstore/product/product_list.html'
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available = True)
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category = category)

    return render(request, templates,
        {
            'category': category,
            'categories': categories,
            'products': products
        }
    )

def product_detail(request, id, slug):
    templates = 'webstore/product/product_detail.html'
    product = get_object_or_404(Product, id = id, slug = slug, available = True)
    category = None
    categories = Category.objects.all()
    basket_product_form = BasketAddProductForm()
    return render(request, templates,
        {
        'product': product,
        'category': category,
        'categories': categories,
        'basket_product_form': basket_product_form
        }
    )