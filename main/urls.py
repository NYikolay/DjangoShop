from django.urls import path

from .views import \
    HomePage,\
    ProductCreateView, \
    ProductUpdateView,\
    PurchaseCreateView, \
    PurchasePageView, \
    ReturnPurchaseView, \
    PurchaseReturnView, \
    DeleteReturn, \
    DeletePurchase

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('create_product', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('create_purchase/', PurchaseCreateView.as_view(), name='create_purchase'),
    path('purchase/', PurchasePageView.as_view(), name='purchase'),
    path('purchase_return/', ReturnPurchaseView.as_view(), name='return_purchase'),
    path('return_purchase/', PurchaseReturnView.as_view(), name='return_page'),
    path('delete_return/<int:pk>/', DeleteReturn.as_view(), name='delete_return'),
    path('delete_purchase/<int:pk>/', DeletePurchase.as_view(), name='delete_purchase'),
]