from rest_framework import serializers
from .models import Store
from .models import Product


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_id', 'store_location']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['Product_id', 'Product_Name', 'Product_timestamp']



    
