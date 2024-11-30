from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer 
class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()  
        self.menu_item_1 = Menu.objects.create(
            title='Pasta',
            price=12.99,
            inventory=100
        )
        self.menu_item_2 = Menu.objects.create(
            title='Pizza',
            price=10.99,
            inventory=90
        )
        self.url = '/restaurant/menu/' 

    def test_getall(self):
        
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = MenuSerializer([self.menu_item_1, self.menu_item_2], many=True).data

        self.assertEqual(response.data, expected_data)
