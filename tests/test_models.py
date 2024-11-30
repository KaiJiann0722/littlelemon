from django.test import TestCase
from restaurant.models import Menu

# TestCase class


class MenuTest(TestCase):
    def test_menu_str_method(self):
        menu_item = Menu.objects.create(
            title='Pasta',
            price=12.99,
            inventory=100
        )
        self.assertEqual(str(menu_item), 'Pasta - 12.99')
