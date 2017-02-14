from django.test import SimpleTestCase
from bs4 import BeautifulSoup
from django.test import Client


class TestAllSPFAMTElements(SimpleTestCase):
    # Test that the navigation bar menu exists on all pages in the Case app
    def test_nav_bar_exists_on_all_case_pages(self):
        client = Client()
        source_code = client.get('spfa_mt.urls')
        soup = BeautifulSoup(source_code.content, "html.parser")
        navtag = soup.findAll("div", attrs={'for': True})
        for div in navtag:
            self.assertTrue(div.has_attr("navbar"))
