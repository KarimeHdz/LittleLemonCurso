from . import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')  


urlpatterns = [
    path('menu-item/', views.MenuItemView.as_view()),
    path('menu-item/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)
]