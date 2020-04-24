import unittest
import allure
from common_utilities import config
from common_utilities.selenium_driver import browser
from pages.login import Login
from pytest import ExitCode

class BaseTest(unittest.TestCase):
    @allure.step("setUp")
    def setUp(self):
        self.driver = browser()
        self.driver.get(config.test_url)
        self.login = Login(self.driver) #page

    @allure.step("tearDown")
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
