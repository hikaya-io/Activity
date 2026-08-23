from unittest.mock import patch
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from workflow.models import Organization, UserInvite


class RegistrationFlowTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register', kwargs={'invite_uuid': 'none'})

    def test_registration_page_renders(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_successful_signup_flow(self):
        data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'username': 'janedoe',
            'email_address': 'janedoe@example.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!',
        }
        with patch('activity.views.send_single_mail') as mock_email:
            mock_email.return_value = 1
            response = self.client.post(self.register_url, data)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'registration/confirm_email.html')
            self.assertTrue(User.objects.filter(username='janedoe').exists())
            user = User.objects.get(username='janedoe')
            self.assertFalse(user.is_active)
            self.assertEqual(user.email, 'janedoe@example.com')

    def test_signup_duplicate_email_shows_friendly_message(self):
        User.objects.create_user(
            username='existinguser',
            email='duplicate@example.com',
            password='Password123!'
        )
        data = {
            'first_name': 'Another',
            'last_name': 'User',
            'username': 'newuser',
            'email_address': 'duplicate@example.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!',
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')
        self.assertIn('message_email', response.context)
        self.assertIn('email already exists', response.context['message_email'].lower())

    def test_signup_duplicate_username_shows_friendly_message(self):
        User.objects.create_user(
            username='takenusername',
            email='first@example.com',
            password='Password123!'
        )
        data = {
            'first_name': 'Another',
            'last_name': 'User',
            'username': 'takenusername',
            'email_address': 'second@example.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!',
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')
        self.assertIn('message_username', response.context)
        self.assertIn('username already exists', response.context['message_username'].lower())

    def test_signup_missing_required_fields_shows_error_message(self):
        data = {
            'first_name': '',
            'last_name': '',
            'username': '',
            'email_address': '',
            'password': '',
            'confirm_password': '',
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_signup_mail_failure_handling(self):
        data = {
            'first_name': 'Test',
            'last_name': 'EmailFail',
            'username': 'emailfailuser',
            'email_address': 'fail@example.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!',
        }
        with patch('activity.views.send_single_mail', side_effect=Exception('SMTP Connection Error')):
            response = self.client.post(self.register_url, data)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'registration/register.html')
            # User should be cleaned up on failure
            self.assertFalse(User.objects.filter(username='emailfailuser').exists())
