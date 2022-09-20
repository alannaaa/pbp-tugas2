from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def test_show_html_resolved(self):  
        response = Client() .get(reverse("mywatchlist:show_mywatchlist"))
        self.assertEqual(response.status_code, 200)
    
    def test_show_xml_resolved(self):         
        response = Client().get(reverse("mywatchlist:show_xml"))
        self.assertEqual(response.status_code, 200)
    
    def test_show_json_resolved(self):         
        response = Client().get(reverse("mywatchlist:show_json"))
        self.assertEqual(response.status_code, 200)