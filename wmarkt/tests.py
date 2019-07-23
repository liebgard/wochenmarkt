from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from wmarkt.views import home
from wmarkt.views import about
from wmarkt.views import register
from django.contrib import admin


class TestHomePage(TestCase):

    def test_root_url_resolves_to_home_function(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)

    #  bad example -- shouldn't be testing constants
    #  better to user render_to_string template function
        self.assertIn(b'<html>', response.content)
        self.assertIn(b'<title>Wochenmarkt</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

class TestAboutPage(TestCase):
    def test_about_url_resolves_to_about_page_function(self):
        found = resolve('/about/')
        self.assertEqual(found.func, about)

    def test_about_url(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)


class TestRegisterPage(TestCase):

    def test_register_url_resolves_register_page_function(self):
        found = resolve('/register/')
        self.assertEqual(found.func, register)

    def test_register_page_returns_correct_html(self):
        request = HttpRequest()
        response = register(request)
        #  bad example -- shouldn't be testing constants
        #  better to user render_to_string template function
        self.assertIn(b'<html>', response.content)
        self.assertIn(b'<title>Wochenmarkt</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
