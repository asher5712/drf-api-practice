from rest_framework import serializers
from .models import MenuItem, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']
        
class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True)
    category_id = serializers.IntegerField(write_only = True)
    
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'category', 'category_id']
        extra_kwargs = {
            'stock' : {'source': 'inventory', 'min_value': 0}
        }