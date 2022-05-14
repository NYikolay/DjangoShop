from datetime import timedelta

from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Product, Purchase, ReturnPurchase
from .forms import CreateProductForm, PurchaseForm, PurchaseReturnForm
from users.models import User


class HomePage(ListView):
    model = Product
    template_name = 'main/home.html'
    extra_context = {'purchase_form': PurchaseForm, }


class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'is_superuser'
    model = Product
    form_class = CreateProductForm
    template_name = 'main/create_product.html'
    success_url = '/'


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'is_superuser'
    model = Product
    fields = '__all__'
    template_name = 'main/update_product.html'
    success_url = '/'


class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'main/purchase_create.html'
    success_url = '/'

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        product = Product.objects.get(id=self.request.POST['product_id'])
        amount_of_money = product.price * object.quantity_of_products
        if amount_of_money > object.user.wallet:
            messages.error(self.request, 'Недостаточно средств')
            return redirect('home')
        elif product.quantity_in_stock < object.quantity_of_products:
            messages.error(self.request, 'Недостаточно товара в наличии')
            return redirect('home')
        product.quantity_in_stock -= object.quantity_of_products
        user = self.request.user
        user.wallet -= amount_of_money
        object.product_id = self.request.POST['product_id']
        user.save()
        object.save()
        product.save()
        return super().form_valid(form=form)


class ReturnPurchaseView(CreateView):
    model = ReturnPurchase
    form_class = PurchaseReturnForm
    template_name = 'main/return_purchase.html'
    success_url = '/purchase/'

    def form_valid(self, form):
        object = form.save(commit=False)
        purchase = Purchase.objects.get(id=self.request.POST['purchase_id'])
        returns = ReturnPurchase.objects.filter(purchase=purchase)
        if purchase.created_at + timedelta(seconds=60 * 3) < timezone.now():
            messages.error(self.request, 'Извините, но время для возврата товара вышло, вы не уложились в три минуты!')
            return redirect('purchase')
        elif returns:
            messages.info(self.request, 'Ваш запрос на возврат принят в обработку!')
            return redirect('purchase')
        messages.info(self.request, 'Ваш запрос отправлен в обработку!')
        object.purchase = purchase
        object.save()
        return super().form_valid(form=form)


class PurchasePageView(ListView):
    model = Purchase
    template_name = 'main/purchase_create.html'

    def get_queryset(self):
        if not self.request.user.is_admin:
            return super().get_queryset().filter(user=self.request.user)
        else:
            return super(PurchasePageView, self).get_queryset()


class PurchaseReturnView(PermissionRequiredMixin, ListView):
    permission_required = 'is_superuser'
    model = ReturnPurchase
    template_name = 'main/return_purchase.html'


class DeleteReturn(PermissionRequiredMixin, DeleteView):
    permission_required = 'is_superuser'
    model = ReturnPurchase
    template_name = 'main/delete_return.html'
    success_url = '/'


class DeletePurchase(PermissionRequiredMixin, DeleteView):
    permission_required = 'is_superuser'
    model = Purchase
    template_name = 'main/delete_purchase.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        product_pk = self.request.POST['product_pk']
        product_price = self.request.POST['product_price']
        purchase_quantity = self.request.POST['purchase_quantity']
        purchase_user = self.request.POST['purchase_user']
        product = Product.objects.get(id=product_pk)
        user = User.objects.get(id=purchase_user)
        product.quantity_in_stock += int(purchase_quantity)
        user.wallet += int(product_price) * int(purchase_quantity)
        user.save()
        product.save()
        return super().post(request, *args, **kwargs)



