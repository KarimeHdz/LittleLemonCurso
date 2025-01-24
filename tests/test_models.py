from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_instance(self):
        # Crear una instancia del modelo Menu
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)

        # Comprobar la representación en cadena
        self.assertEqual(str(item), "IceCream : 80")
