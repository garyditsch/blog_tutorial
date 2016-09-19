from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.

class BlogViewsTests(TestCase):

    def test_views_index(self):
        index_url = reverse('blog:index')

        response = self.client.get(index_url)
        self.assertEqual(response.status_code, 200)