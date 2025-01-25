from django.shortcuts import render
#from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
#from .models import MenuItem 
#from .serializers import MenuItemSerializer
#from django.http import HttpResponse
#from django.contrib.auth.models import User
##from rest_framework import viewsets
#from rest_framework.permissions import IsAuthenticated
#from .serializers import UserSerializer
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer

# Create your views here.
#def sayHello(request):
#    return HttpResponse('Hello world')

def index(request):
    return render(request, 'index.html')


class MenuItemView(generics.ListCreateAPIView):
     permission_classes = [IsAuthenticated]
     queryset = MenuItem.objects.all()
     serializer_class = MenuItemSerializer
     
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemViewSet(ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()  
    serializer_class = BookingSerializer 

#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 
   
#class MenuItemView(ModelViewSet):
#    queryset = MenuItem.objects.all()
#    serializer_class = MenuItemSerializer