from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem
from .serializers import MenuItemSerialzier

# Create your views here.
@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        # SQL queries must not be used till necessary and if used then 
        # values must be used as parameterized list as shown below
        limit = request.GET.get('limit')
        items = MenuItem.objects.select_related('category').all()
        if limit:
            items = MenuItem.objects.raw('SELECT * FROM LittleLemonAPI_menuitem LIMIT %s', [limit]) 
        
        serialized_item = MenuItemSerialzier(items, many=True)
        return Response(serialized_item.data)
    
    elif request.method == 'POST':
        serialized_item = MenuItemSerialzier(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        # serialized_item.validated_data # Access validated data
        serialized_item.save()
        # data attribute given below can only be called after invoking save method
        return Response(serialized_item.data, status=status.HTTP_201_CREATED)
        
@api_view()
def single_item(request, id):
    items = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerialzier(items)
    return Response(serialized_item.data)