import allure
from selenium.webdriver.common.by import By
from common_utilities.selenium_driver import SeleniumDriver
from test_data.login_credentials import LoginCredentials


class Login(SeleniumDriver):
    """
    Page sample
    """
    absolute_path = "myaccount.google.com"
    user_name_text = (By.CSS_SELECTOR, 'input[name="identifier"]')
    password_text = (By.CSS_SELECTOR, 'input[name="password"]')
    next_button =(By.CSS_SELECTOR, 'div[id="identifierNext"]')
    password_next_button =(By.CSS_SELECTOR, 'div[id="passwordNext"]')

    @allure.step("Enter User Name")
    def enter_username(self, username):
        self.driver.find_element(*self.user_name_text).send_keys(username)

    @allure.step("Enter Password")
    def enter_password(self, password):
        self.driver.find_element(*self.password_text).send_keys(password)

    @allure.step("Click Next button")
    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    @allure.step("Click Next button")
    def click_password_next_button(self):
        self.driver.find_element(*self.password_next_button).click()

    @allure.step("User Login with Commerce")
    def user_login(self, username=LoginCredentials.username, password=LoginCredentials.password):
        self.enter_username(username)
        self.click_next_button()
        self.enter_password(password)
        self.click_password_next_button()
