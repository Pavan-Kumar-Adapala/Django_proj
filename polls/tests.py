from django.test import TestCase
from django.urls import reverse

class PollAppTestCase(TestCase):
    def test_homepage_status_code(self):
        """Ensure the /poll homepage is reachable."""
        response = self.client.get(reverse('poll:home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_content(self):
        """Ensure a specific text appears in the /poll homepage."""
        response = self.client.get(reverse('poll:home'))
        self.assertContains(response, "Welcome to the Poll App")
