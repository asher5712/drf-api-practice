from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from rest_framework import serializers
from decimal import Decimal
from .models import MenuItem, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerialzier(serializers.ModelSerializer):
    # stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=2)
    # title = serializers.CharField(
    #     max_length=255,
    #     validators=[UniqueValidator(queryset=MenuItem.objects.all())]
    # )
    
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=MenuItem.objects.all(),
        #         fields=['title', 'stock']
        #     ),
        # ]
        extra_kwargs = {
            'price': {'min_value': 2},
            'stock': {'source':'inventory', 'min_value':0},
            'title': {
                'validators': [ 
                    UniqueValidator(
                        queryset=MenuItem.objects.all() # To make sure no duplication of title
                    )
                ]
            }
        }
        
    def calculate_tax(self, product:MenuItem):
        return round(product.price * Decimal(1.1), 2)
    
    # def validate(self, attrs):
    #     if(attrs['price']<2):
    #         raise serializers.ValidationError('Price should not be less than 2.0')
    #     if(attrs['inventory']<0):
    #         raise serializers.ValidationError('Stock cannot be negative')
    #     return super().validate(attrs)
    
    # def validate_price(self, value):
    #     if (value < 2):
    #         raise serializers.ValidationError('Price should not be less than 2.0')
    
    # def validate_stock(self, value):
    #     if (value < 0):
    #         raise serializers.ValidationError('Stock cannot be negative')
    
# Four methods to validate the data (use only one for validation)
# 1st, use built-in '''min_value''' property to validate price
# 2nd, use '''extra_kwargs''' attribute of Meta class, [Note: no need to declare fields above]
# 3rd, use validate_field methods where field is fieldname [Note: fields must be declared somewhere]
# 4th, use validate method where all fields can be validated at once

# Use '''UniqueValidator''' to ensure the objects do not duplicate,
# can be used inside '''extra_kwargs''' or in '''field declaration'''
# ---------------------
# Use '''UniqueTogetherValidator''' to ensure the combination of fields do not repeat,
# is used inside Meta class
