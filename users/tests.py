from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserModelTest(TestCase):
    """
    Test the CustomUser model.
    """

    def test_create_user(self):
        user = User.objects.create_user(
            username='papayaw',
            email='papayaw@example.com',
            password='securepassword123',
            phone_number='0240001111'
        )

        self.assertEqual(user.username, 'papayaw')
        self.assertEqual(user.email, 'papayaw@example.com')
        self.assertEqual(user.phone_number, '0240001111')
        self.assertTrue(user.check_password('securepassword123'))


class UserAuthViewsTest(TestCase):
    """
    Test registration and login views.
    """

    def test_register_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'phone_number': '0241112222',
            'password1': 'StrongPassword123',
            'password2': 'StrongPassword123',
        })

        # Should redirect after successful registration
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_view(self):
        user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )

        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword123'
        })

        # Successful login redirects
        self.assertEqual(response.status_code, 302)