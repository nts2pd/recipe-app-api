from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating new user with a successful email"""
        email = 'test@fakemail.com'
        password = '123123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email for new user is normalized"""
        email = 'fake@fakeemail.com'
        user = get_user_model().objects.create_user(email, '123123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_user(self):
        """test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123123')

    def test_create_new_superuser(self):
        """test creating new superuser"""
        user = get_user_model().objects.create_superuser(
            'fake@fakemail.com',
            '123123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
