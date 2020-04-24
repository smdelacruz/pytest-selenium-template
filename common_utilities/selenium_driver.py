from selenium import webdriver


class SeleniumDriver:
    def __init__(self, selenium_driver):
        self.driver = selenium_driver


def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver
