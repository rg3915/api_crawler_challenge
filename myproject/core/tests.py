
from django.test import TestCase
from myproject.core.crawler import contains_http, get_text_content


class APIGetTest(TestCase):
    """Tests for API GET Method."""

    def setUp(self):
        self.res = self.client.get('/api/?url=python.org&w=Python')

    def test_get(self):
        """Must return status code 200."""
        self.assertEqual(200, self.res.status_code)

    def test_content(self):
        """Response must contain word chosen (Python) and its number of word occurrences (98)."""
        CONTENTS = ('Python', '98')

        for content in CONTENTS:
            with self.subTest():
                self.assertContains(self.res, content)


class CrawlerTest(TestCase):
    """Tests for crawler."""

    def test_response_content(self):
        """Response must return website content."""
        res = get_text_content('http://www.python.org')
        self.assertTrue(res)


class UrlSchemesTest(TestCase):
    """Tests for HTTP/HTTPS schemes."""

    def test_url_not_contains_http(self):
        """Must add scheme HTTP in the beginning of the URL."""
        url = 'www.python.org'
        self.assertEqual('http://' + url, contains_http(url))

    def test_url_contains_http(self):
        """Must keep the URL the same when they have either HTTP or HTTPS schema."""
        urls = ['http://www.python.org', 'https://www.python.org']
        for url in urls:
            with self.subTest():
                self.assertEqual(url, contains_http(url))
