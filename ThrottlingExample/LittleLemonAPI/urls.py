from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.MenuItemViewSet.as_view({'get':'list'})),
    path('menu-items/<int:pk>', views.MenuItemViewSet.as_view({'get':'retrieve'})),
    
]