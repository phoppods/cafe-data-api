from django.urls import path
from .views import StoreDetailUpdateDelete, StoreList
from .views import ProductDetailUpdateDelete, ProductList
from .views import SaleDetailUpdateDelete, SaleList

urlpatterns = [
    path('stores/', StoreList.as_view(), name='store_list'),
    path('stores/<int:store_id>/',
         StoreDetailUpdateDelete.as_view(), name='store_detail'),

    path('products/', ProductList.as_view(), name='product_id'),
    path('products/<int:product_id>/',
         ProductDetailUpdateDelete.as_view(), name='product_name'),

    path('sales/', SaleList.as_view(), name='sale_list'),
    path('sales/<int:transaction_id>/',
         SaleDetailUpdateDelete.as_view(), name='sale_detail'),
]
