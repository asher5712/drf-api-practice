from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from rest_framework import serializers
from decimal import Decimal
from .models import MenuItem, Category
import bleach


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerialzier(serializers.ModelSerializer):
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']
        extra_kwargs = {
            'price': {'min_value': 2},
            'stock': {'source':'inventory', 'min_value':0},
        }
        
    def calculate_tax(self, product:MenuItem):
        return round(product.price * Decimal(1.1), 2)
    
    # '''bleach''' can be used with validate_field as well as validate
    def validate_title(self, value):
        return bleach.clean(value)
