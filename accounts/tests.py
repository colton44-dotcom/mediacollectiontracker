from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class AuthenticationTests(TestCase):
    """Tests for registration, login, and logout flows."""

    def setUp(self):
        """Create a test user and client before each test."""
        self.client = Client()
        self.username = "testuser"
        self.password = "SecurePass123!"
        self.user = User.objects.create_user(
            username=self.username,
            email="test@example.com",
            password=self.password,
        )

    # ---------- Registration ----------

    def test_registration_success(self):
        """A new user can register and is redirected home."""
        url = reverse("register")
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password1": "ComplexPass456!",
            "password2": "ComplexPass456!",
        }
        response = self.client.post(url, data, follow=True)

        # User was created
        self.assertTrue(User.objects.filter(username="newuser").exists())
        # Redirected to home
        self.assertRedirects(response, reverse("home"))

    def test_registration_password_mismatch(self):
        """Registration fails when passwords don't match."""
        url = reverse("register")
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password1": "ComplexPass456!",
            "password2": "DifferentPass789!",
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)  # re-rendered form
        self.assertFalse(User.objects.filter(username="newuser").exists())

    def test_registration_duplicate_username(self):
        """Registration fails if username already exists."""
        url = reverse("register")
        data = {
            "username": self.username,  # already taken
            "email": "other@example.com",
            "password1": "ComplexPass456!",
            "password2": "ComplexPass456!",
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.filter(username=self.username).count(), 1)

    # ---------- Login ----------

    def test_login_success(self):
        """Valid credentials log the user in and redirect home."""
        url = reverse("login")
        response = self.client.post(
            url,
            {"username": self.username, "password": self.password},
            follow=True,
        )

        self.assertTrue(response.context["user"].is_authenticated)
        self.assertRedirects(response, reverse("home"))

    def test_login_invalid_password(self):
        """Wrong password leaves the user anonymous."""
        url = reverse("login")
        response = self.client.post(
            url,
            {"username": self.username, "password": "WrongPassword!"},
        )

        self.assertEqual(response.status_code, 200)  # form re-rendered
        self.assertFalse(response.context["user"].is_authenticated)

    def test_login_nonexistent_user(self):
        """Unknown username leaves the user anonymous."""
        url = reverse("login")
        response = self.client.post(
            url,
            {"username": "ghost", "password": "whatever"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["user"].is_authenticated)

    # ---------- Logout ----------

    def test_logout_success(self):
        """A logged-in user can log out via POST."""
        self.client.login(username=self.username, password=self.password)
        url = reverse("logout")
        response = self.client.post(url, follow=True)

        self.assertFalse(response.context["user"].is_authenticated)
        self.assertRedirects(response, reverse("home"))

    def test_logout_requires_post(self):
        """GET request to logout returns 405 Method Not Allowed."""
        self.client.login(username=self.username, password=self.password)
        url = reverse("logout")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 405)