from django.shortcuts import render, get_object_or_404
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer
from rest_framework_csv.renderers import CSVRenderer
from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your views here.
@api_view()
# @renderer_classes([CSVRenderer]) # Displays CSV Response instead of default JSON in Insomnia
# @renderer_classes([XMLRenderer]) # Displays XML Response instead of default JSON in Insomnia
# @renderer_classes([YAMLRenderer]) # Displays YAML Response instead of default JSON in Insomnia
def menu_items(request):
    items = MenuItem.objects.select_related('category').all() 
    serialized_item = MenuItemSerializer(items, many=True)
    return Response(serialized_item.data)

@api_view()
def single_item(request, id):
    items = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(items)
    return Response(serialized_item.data)

@api_view() 
@renderer_classes ([TemplateHTMLRenderer])
def menu(request):
    items = MenuItem.objects.select_related('category').all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response({'data':serialized_item.data}, template_name='menu-items.html')

@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def welcome(request):
    data = '<html><body><h1>Welcome To Little Lemon API Project</h1></body></html>'
    return Response(data)