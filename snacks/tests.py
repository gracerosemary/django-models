from django.test import TestCase
from django.http import response
from django.urls import reverse
from .models import Snack

class DemoTest(TestCase):
    def test_home_page_status(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
    
    def test_base_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')
    
    # need to figure out how to test pk
    # def test_detail_page_status(self):
    #     url = reverse('snack_details')
    #     response = self.client.get(url)
    #     self.assertEquals(response, 'snack_details.html')
