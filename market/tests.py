from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Item

User = get_user_model()


class ItemModelTest(TestCase):
    """
    Test Item model creation.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username='seller',
            password='sellerpassword123'
        )

    def test_create_item(self):
        item = Item.objects.create(
            title='Laptop',
            description='A powerful laptop',
            price=5000.00,
            owner=self.user,
            phone_number='0240000000',
            is_active=True
        )

        self.assertEqual(item.title, 'Laptop')
        self.assertEqual(item.owner.username, 'seller')
        self.assertTrue(item.is_active)


class ItemViewsTest(TestCase):
    """
    Test item list and detail views.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username='seller',
            password='sellerpassword123'
        )

        self.active_item = Item.objects.create(
            title='Active Product',
            description='Visible product',
            price=100.00,
            owner=self.user,
            phone_number='0240000000',
            is_active=True
        )

        self.inactive_item = Item.objects.create(
            title='Inactive Product',
            description='Hidden product',
            price=200.00,
            owner=self.user,
            phone_number='0240000000',
            is_active=False
        )

    def test_item_list_view_shows_only_active_items(self):
        response = self.client.get(reverse('item_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Active Product')
        self.assertNotContains(response, 'Inactive Product')

    def test_item_detail_view_active_item(self):
        response = self.client.get(
            reverse('item_detail', args=[self.active_item.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Visible product')

    def test_item_detail_view_inactive_item_returns_404(self):
        response = self.client.get(
            reverse('item_detail', args=[self.inactive_item.pk])
        )

        self.assertEqual(response.status_code, 404)