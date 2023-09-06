from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MenuItem, Category
from .serializers import MenuItemSerialzier, CategorySerializer

# Create your views here.
@api_view()
def menu_items(request):
    items = MenuItem.objects.select_related('category').all()
    serialized_item = MenuItemSerialzier(items, many=True, context={'request': request})
    return Response(serialized_item.data)

@api_view()
def single_item(request, id):
    items = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerialzier(items)
    return Response(serialized_item.data)

@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data)

