from django.test import TestCase
from django.urls import reverse

from .models import Item


class ItemModelTests(TestCase):
    def test_item_creation_and_str(self):
        item = Item.objects.create(
            name="Test Item",
            description="Test description",
            price=9.99,
            stock=5,
        )
        self.assertEqual(str(item), "Test Item")
        self.assertEqual(Item.objects.count(), 1)


class ItemViewTests(TestCase):
    def setUp(self):
        self.item = Item.objects.create(
            name="Test Item",
            description="Test description",
            price=9.99,
            stock=5,
        )

    def test_item_list_view(self):
        url = reverse('item_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data['items']), 1)
        self.assertEqual(data['items'][0]['name'], self.item.name)

    def test_item_detail_view(self):
        url = reverse('item_detail', args=[self.item.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['item']['name'], self.item.name)

    def test_item_detail_view_not_found(self):
        url = reverse('item_detail', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
