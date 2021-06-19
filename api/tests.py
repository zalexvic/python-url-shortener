from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Link


# Create your tests here.
class ShortenerViewSetTestCase(APITestCase):

    def test_url_list(self):
        url = reverse('all_links')
        response = self.client.get(url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_create_link_url(self):
        url = reverse('create_link')
        source_link = 'https://google.com'
        response = self.client.post(url, data={'source_link': source_link})
        short_link = response.json()['short_link']

        self.assertEquals(Link.objects.get(id=1).short_link, short_link)

    def test_create_link_no_data(self):
        url = reverse('create_link')
        response = self.client.post(url)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_redirect_from_short_link(self):
        create_link_url = reverse('create_link')
        source_link = 'https://google.com'
        response = self.client.post(create_link_url, data={'source_link': source_link})
        short_link = response.json()['short_link']

        response = self.client.get('http://' + short_link)

        self.assertEquals(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
