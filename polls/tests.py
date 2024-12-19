from django.test import TestCase
from django.urls import reverse
from .models import Question, Choice
from django.utils.timezone import now

class PollsAppTests(TestCase):


    def test_index_view_status_code(self):
        """Test if the index view returns a 200 status code."""
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)

    def test_owner_view(self):
        """Test the owner view response."""
        response = self.client.get(reverse('polls:owner'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world. a8c5a734 is the polls owner.")
