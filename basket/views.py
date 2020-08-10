from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from webstore.models import Product, Category
from .basket import Basket
from .forms import BasketAddProductForm


@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id = product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(product = product, quantity = cd['quantity'], update_quantity = cd['update'])
    return redirect('basket:basket_detail')

def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id = product_id)
    basket.remove(product)
    return redirect('basket:basket_detail')

def basket_detail(request):
    category = None
    categories = Category.objects.all()
    templates = 'basket/basket_detail.html'
    basket = Basket(request)
    return render(request, templates, 
        {
        'basket': basket,
        'category': category,
        'categories': categories
        }
    )
