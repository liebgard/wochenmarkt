import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()


    def test_title_is_correct(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Wochenmarkt', self.browser.title)
        self.assertTrue(self.browser.find_element_by_link_text('Startseite'))
        self.assertTrue(self.browser.find_element_by_link_text('Über uns'))
        self.assertTrue(self.browser.find_element_by_link_text('Login'))
        self.assertTrue(self.browser.find_element_by_link_text('Register'))
        rezepte = (self.browser.find_elements_by_tag_name('h2'))
        self.assertTrue(any(rezept.text == 'Rezept 1' for rezept in rezepte))


class AdminPageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    #  use inputbox.send_Keys
    def test_admin_login_page(self):
        self.browser.get('http://localhost:8000/admin/')
        self.assertIn('Log in | Django site admin', self.browser.title)


if __name__ == '__main__':
    unittest.main()
