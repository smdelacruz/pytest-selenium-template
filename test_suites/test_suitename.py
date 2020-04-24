import pytest
import allure
from common_utilities import basetest


@allure.feature("GUI Test")
class UITest(basetest.BaseTest):
    """
    Only Sample Test Suite Class
    """

    def test_case_sample(self):
        """
        Only Sample Test Case
        :return:
        """
        expected_url = self.login.absolute_path()
        self.login.user_login()
        self.assertEqual(expected_url, self.driver.current_url, "Actual Url - {} is incorrect".format(self.driver.current_url))
