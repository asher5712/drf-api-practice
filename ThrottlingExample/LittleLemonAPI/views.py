from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .models import MenuItem
from .serializers import MenuItemSerializer
from .throttling import TenCallPerMinute

# Create your views here.
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    throttle_classes = [
        AnonRateThrottle,
        UserRateThrottle,
        # TenCallPerMinute # Custom throttle class in class-based view
    ]
    
    # Custom Throttle check post request
    # def get_throttles(self):
    #     if self.action == 'create':
    #         throttle_classes = [UserRateThrottle]
    #     else:
    #         throttle_classes = []
    #     return [throttle() for throttle in throttle_classes]