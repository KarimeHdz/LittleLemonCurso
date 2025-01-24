from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
#def sayHello(request):
#    return HttpResponse('Hello world')

#def index(request):
#    return render(request, 'index.html')


class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 
   
@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
# 
def msg(request):
    return Response({"message":"This view is protected"})