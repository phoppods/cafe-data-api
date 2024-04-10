from rest_framework import generics
from .models import Store
from .serializers import StoreSerializer
from .models import Product
from .serializers import ProductSerializer
from .models import Sale
from .serializers import SaleSerializer

# provides both list (GET) and create (POST) functionalities


class StoreList(generics.ListCreateAPIView):
    # fetches all Store objects from the database.
    queryset = Store.objects.all()
    # for serializing/deserializing data to JSON when interacting with the view
    serializer_class = StoreSerializer

# provides built-in functionality for retrieving, updating, and deleting a single object.

class StoreDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    lookup_field = 'store_id'


class ProductList(generics.ListCreateAPIView):
   
    queryset = Product.objects.all()
    
    serializer_class = ProductSerializer
class ProductDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'product_id'


    
class SaleList(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    lookup_field = 'transaction_id'


        