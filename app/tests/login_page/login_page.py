from app.tests.utilities import selenium_utility


class Login(selenium_utility.SeleniumUtility):
    _login_input = '//input[@id="login-username"]'
    _password_input = '//input[@id="login-password"]'
    _login_btn = '//button[@id="login-button"]'
    _agree_btn = '//button[@id="auth-accept"]'
    _playlists_list = '//ul[@class="list-group"]'

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def login(self, login_name, password):
        login_input = self.wait_for_element(self._login_input)
        login_input.click()
        login_input.send_keys(login_name)

        password_input = self.driver.find_element_by_xpath(self._password_input)
        password_input.click()
        password_input.send_keys(password)

        login_btn = self.driver.find_element_by_xpath(self._login_btn)
        login_btn.click()
        agree_btn = self.wait_for_element(self._agree_btn)
        agree_btn.click()

    def get_playlists(self):
        return self.wait_for_element(self._playlists_list)
