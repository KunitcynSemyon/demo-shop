from django import forms
from webstore.models import Product

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class BasketAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices = PRODUCT_QUANTITY_CHOICES, coerce = int)
    update = forms.BooleanField(required = False, initial = False, widget = forms.HiddenInput)