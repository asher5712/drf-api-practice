from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerialzier

# Create your views here.
@api_view()
def menu_items(request):
    # items = MenuItem.objects.select_related('category').all()  # Use select_related with StringRelated serializer field
    items = MenuItem.objects.all()
    serialized_item = MenuItemSerialzier(items, many=True)
    return Response(serialized_item.data)

@api_view()
def single_item(request, id):
    items = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerialzier(items)
    return Response(serialized_item.data)