import unittest
from selenium import webdriver
import time

class AdminPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(10)
        cls.browser.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()

    #  use inputbox.send_Keys
    def test_admin_login_page_password_invalid(self):
        self.browser.get('http://localhost:8000/admin/')
        self.assertIn('Log in | Django site admin', self.browser.title)
        self.assertIn("Django administration", self.browser.find_element_by_id("site-name").text)
        username = "Admin"
        self.browser.find_element_by_id("id_username").send_keys(username)
        self.browser.find_element_by_id("id_password").send_keys("admin1234")
        self.browser.find_element_by_class_name("submit-row").click()
        self.assertTrue(self.browser.find_element_by_class_name("errornote"))

    def test_admin_login_page_password_valid(self):
        self.browser.get('http://localhost:8000/admin/')
        self.assertIn('Log in | Django site admin', self.browser.title)
        username = "Admin"
        userpw = "admin2019"
        self.browser.find_element_by_id("id_username").send_keys(username)
        self.browser.find_element_by_id("id_password").send_keys(userpw)
        self.browser.find_element_by_class_name("submit-row").click()
        time.sleep(2)
        self.assertIn("Django administration", self.browser.find_element_by_id("site-name").text)
        self.assertTrue(self.browser.find_element_by_class_name("errornote"))
        self.browser.find_element_by_link_text("Change password")
        self.browser.find_element_by_link_text("Log out").click

    def test_admin_groups(self):
        self.browser.get('http://localhost:8000/admin/')
        self.assertIn('Log in | Django site admin', self.browser.title)
        username = "Admin"
        userpw = "admin2019"
        self.browser.find_element_by_id("id_username").send_keys(username)
        self.browser.find_element_by_id("id_password").send_keys(userpw)
        self.browser.find_element_by_class_name("submit-row").click()
        time.sleep(2)
        self.assertIn("Django administration", self.browser.find_element_by_id("site-name").text)
        self.browser.find_element_by_link_text("Groups").click()
        time.sleep(2)
        self.assertIn("Select group to change", self.browser.find_element_by_id("content").text)
        self.browser.find_element_by_xpath("//*[@id='user-tools']/a[3]").click()

    def test_admin_groups_navigate_breadcrumb(self):
        self.browser.get('http://localhost:8000/admin/')
        self.assertIn('Log in | Django site admin', self.browser.title)
        username = "Admin"
        userpw = "admin2019"
        self.browser.find_element_by_id("id_username").send_keys(username)
        self.browser.find_element_by_id("id_password").send_keys(userpw)
        self.browser.find_element_by_class_name("submit-row").click()
        time.sleep(2)
        self.assertIn("Django administration", self.browser.find_element_by_id("site-name").text)
        self.browser.find_element_by_link_text("Groups").click()
        time.sleep(2)
        self.assertIn("Select group to change", self.browser.find_element_by_id("content").text)
        self.browser.find_element_by_xpath("//*[@id='container']/div[2]/a[2]").click()
        userButtonText = self.browser.find_element_by_xpath("//*[@id='content-main']/div/table/tbody/tr[2]/th/a").text
        self.assertIn("Users", userButtonText)
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='user-tools']/a[3]").click()

    def test_admin_users(self):
        self.browser.get('http://localhost:8000/admin/')
        self.assertIn('Log in | Django site admin', self.browser.title)
        username = "Admin"
        userpw = "admin2019"
        self.browser.find_element_by_id("id_username").send_keys(username)
        self.browser.find_element_by_id("id_password").send_keys(userpw)
        self.browser.find_element_by_class_name("submit-row").click()
        time.sleep(2)
        self.assertIn("Django administration", self.browser.find_element_by_id("site-name").text)
        userListLink = self.browser.find_element_by_xpath("//*[@id='content-main']/div/table/tbody/tr[2]/th/a")
        userListLink.click()
        self.assertIn("Select user to change", self.browser.find_element_by_id("content").text)
        time.sleep(2)
        # logout
        self.browser.find_element_by_xpath("//*[@id='user-tools']/a[3]").click()


    def test_admin_user_edit(self):
        self.browser.get('http://localhost:8000/admin/')
        username = "Admin"
        userpw = "admin2019"
        self.browser.find_element_by_id("id_username").send_keys(username)
        self.browser.find_element_by_id("id_password").send_keys(userpw)
        self.browser.find_element_by_class_name("submit-row").click()
        time.sleep(2)
        self.assertIn("Django administration", self.browser.find_element_by_id("site-name").text)
        userListLink = self.browser.find_element_by_xpath("//*[@id='content-main']/div/table/tbody/tr[2]/th/a")
        userListLink.click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='result_list']/tbody/tr/th/a").click()
        self.assertIn("Change user", self.browser.find_element_by_xpath("//*[@id='content']/h1").text)
        time.sleep(2)
        # logout
        self.browser.find_element_by_xpath("//*[@id='user-tools']/a[3]").click()

    def test_admin_user_add(self):
        self.browser.get('http://localhost:8000/admin/')
        username = "Admin"
        userpw = "admin2019"
        self.browser.find_element_by_id("id_username").send_keys(username)
        self.browser.find_element_by_id("id_password").send_keys(userpw)
        self.browser.find_element_by_class_name("submit-row").click()
        time.sleep(2)
        userListLink = self.browser.find_element_by_xpath("//*[@id='content-main']/div/table/tbody/tr[2]/th/a")
        userListLink.click()
        time.sleep(2)
        # Click Button to Add User
        self.browser.find_element_by_xpath("//*[@id='content-main']/ul/li/a").click()
        self.assertIn("Add user", self.browser.find_element_by_xpath("//*[@id='content']/h1").text)
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='id_username']").send_keys("Testuser1")
        self.browser.find_element_by_xpath("//*[@id='id_password1']").send_keys("testing456")
        self.browser.find_element_by_xpath("// *[ @ id = 'id_password2']").send_keys("testing456")
        # Save and continue editing
        self.browser.find_element_by_xpath("// *[ @ id = 'user_form'] / div / div / input[3]").click()
        # Check User was added successfully
        self.assertIn("was added successfully", self.browser.find_element_by_xpath("// *[ @ id = 'container'] / ul / li").text)
        self.browser.find_element_by_xpath("// *[ @ id = 'id_email']").send_keys("testuser1@bssm.de")
        time.sleep(2)
        # Save email address
        self.browser.find_element_by_xpath("// *[ @ id = 'user_form'] / div / div / input[1]").click()
        time.sleep(2)
        # logout
        self.browser.find_element_by_xpath("//*[@id='user-tools']/a[3]").click()


if __name__ == '__main__':
    unittest.main()
