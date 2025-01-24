from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.test import TestCase

class MenuViewTest(TestCase):
    def setUp(self):
        # Crear instancias de prueba del modelo Menu
        Menu.objects.create(title="Pizza", price=12.99, inventory=50)
        Menu.objects.create(title="Burger", price=8.99, inventory=30)
        Menu.objects.create(title="Pasta", price=10.99, inventory=20)

    def test_getall(self):
        # Recuperar todos los objetos Menu
        menus = Menu.objects.all()
        
        # Serializar los datos recuperados
        serialized_data = MenuSerializer(menus, many=True).data

        # Realizar aserciones
        self.assertEqual(len(serialized_data), 3)
        self.assertEqual(serialized_data[0]['title'], "Pizza")
        self.assertEqual(serialized_data[1]['title'], "Burger")
        self.assertEqual(serialized_data[2]['title'], "Pasta")