import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # Create Firefox browser for running automations
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        # Run the same test as in python_org_search_basic.py

        # Load website
        self.driver.get("http://www.python.org")

        # Ensure website loaded
        self.assertIn("Python", driver.title)

        # Send input to page
        elem = self.driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)

        # Make sure correct results loaded
        assert "No results found." not in self.driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
