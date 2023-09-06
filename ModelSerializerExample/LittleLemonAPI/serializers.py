from rest_framework import serializers
from decimal import Decimal
from .models import MenuItem

class MenuItemSerialzier(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax']
        
    def calculate_tax(self, product:MenuItem):
        return round(product.price * Decimal(1.1), 2)