from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views

urlpatterns = [
    path('category', views.CategoriesView.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
    path('secret', views.secret),
    path('api-token-auth', obtain_auth_token),
    path('manager', views.manager_view),
    path('throttle-check', views.throttle_check),
    path('throttle-check-auth', views.throttle_check_auth),
    path('user-throttle-check', views.user_throttle_check),
    path('groups/manager/users', views.managers)
]