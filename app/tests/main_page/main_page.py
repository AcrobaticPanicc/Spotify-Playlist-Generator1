from app.tests.utilities import selenium_utility


class MainPage(selenium_utility.SeleniumUtility):
    _login_btn = '//button[@id="login-btn"]'

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def get_main_page_title(self):
        return self.driver.title

    def click_login(self):
        self.driver.find_element_by_xpath(self._login_btn).click()
