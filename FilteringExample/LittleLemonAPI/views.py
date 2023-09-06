from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer

# Create your views here.
@api_view(['GET','POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        if category_name:
            items = items.filter(category__title__iexact = category_name)
        
        if to_price:
            items = items.filter(price__lte = to_price)
            
        if search:
            items = items.filter(title__icontains = search)
        
        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status=status.HTTP_201_CREATED)

@api_view()
def single_item(request, pk):
    item = get_object_or_404(MenuItem, pk = pk)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data, status=status.HTTP_200_OK)