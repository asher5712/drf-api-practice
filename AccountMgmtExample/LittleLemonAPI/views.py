from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer
from .throttling import TenCallsPerMinute
from django.contrib.auth.models import User, Group

# Create your views here.
class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['category']
    
@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({'message':'some secret message'})


@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({'message':'only managers can see this'}, status=status.HTTP_200_OK)
    else:
        return Response({'message':'permission denied'}, status=status.HTTP_403_FORBIDDEN)
    
    
@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({'message': 'successful'})

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def throttle_check_auth(request):
    return Response({'message': 'logged in user request, successful'})

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute])
def user_throttle_check(request):
    return Response({'message': 'logged in authenticated, successful'})

@api_view(['POST','DELETE'])
@permission_classes([IsAdminUser])
def managers(request):
    username = request.data['username']
    if username:
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name="Manager")
        if request.method == 'POST':
            managers.user_set.add(user)
        elif request.method == "DELETE":
            managers.user_set.remove(user)
        return Response({'message':'ok'})
    return Response({'message':'error'}, status=status.HTTP_400_BAD_REQUEST)