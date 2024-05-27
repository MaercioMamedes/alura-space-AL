from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.


class UserTestCase(TestCase):

    def test_create_user(self):

        user = User.objects.create_user(
            username="teste",
            email="teste@teste.com"
        )

        user.set_password("1234")

        user.save()

        self.assertIsInstance(user, User)

