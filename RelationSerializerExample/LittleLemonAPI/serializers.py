from rest_framework import serializers
from decimal import Decimal
from .models import MenuItem, Category


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'slug', 'title']

class MenuItemSerialzier(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # category = serializers.StringRelatedField() # Used to display category string instead of id
    # category = CategorySerializer()
    
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category']
        depth = 1
        
    def calculate_tax(self, product:MenuItem):
        return round(product.price * Decimal(1.1), 2)
    
    
# Two Methods to show relationship in model serializers
# 1st is to use '''category = CategorySerializer()'''
# 2nd is to use '''depth = 1''' in Meta class 
# [Note: for 2nd, no need of declaring CategorySerializer class]