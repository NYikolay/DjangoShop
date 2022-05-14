from django import forms

from .models import Product, Purchase, ReturnPurchase


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'quantity_in_stock', 'image')


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('quantity_of_products',)


class PurchaseReturnForm(forms.ModelForm):
    class Meta:
        model = ReturnPurchase
        fields = []

