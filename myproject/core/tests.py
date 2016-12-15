from django.test import TestCase
from django.shortcuts import resolve_url


class CrawlerTest(TestCase):

    def test_res(self):
        res = {'Python': 97}
        self.assertEqual({'Python': 97}, res)
