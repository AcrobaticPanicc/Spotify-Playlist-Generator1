from selenium.webdriver import ActionChains

from app.tests.utilities import selenium_utility


class FineTune(selenium_utility.SeleniumUtility):
    _danceable_slider = '(//div[@role="slider"])[1]'
    _energy_slider = '(//div[@role="slider"])[3]'
    _loudness_slider = '(//div[@role="slider"])[5]'
    _popularity_slider = '(//div[@role="slider"])[7]'
    _next_btn = '//button[@id="next-btn"]'

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.move = ActionChains(driver)

        self.sliders = [
            self._danceable_slider,
            self._energy_slider,
            self._loudness_slider,
            self._popularity_slider
        ]

    def move_sliders(self):
        for slider in self.sliders:
            found_slider = self.get_element(slider)
            self.move.click_and_hold(found_slider).move_by_offset(40, 0).release().perform()

    def get_sliders_values(self):
        """
        return the current sliders values
        """

        slider_values = []

        for slider in self.sliders:
            found_slider = self.get_element(slider)
            slider_values.append(found_slider.get_attribute('aria-valuenow'))

        return slider_values

    def click_next(self):
        self.scroll_to_element(self._next_btn)
        self.get_element(self._next_btn).click()
