from app.tests.utilities import selenium_utility


class SelectTracks(selenium_utility.SeleniumUtility):
    _first_playlist = '//li[@data-toggle="collapse"][1]'
    _track = '(//li[contains(@class, "track")])[1]'
    _next_btn = '//button[@id="next-btn"]'

    def __init__(self, driver):
        self.driver = driver
        self.first_playlists = None

        from selenium.webdriver.common.action_chains import ActionChains
        self.actions = ActionChains(driver)
        super().__init__(driver)

    def click_next_without_any_selection(self):
        self.scroll_to_element(self._next_btn)
        self.get_element(self._next_btn).click()

    def get_alert_text(self):
        alert = self.driver.switch_to_alert()
        alert_text = alert.text
        alert.accept()
        return alert_text

    def get_first_playlist(self):
        self.first_playlists = self.wait_for_element(self._first_playlist)

    def check_if_expanded(self):
        self.get_first_playlist()
        is_expanded = self.first_playlists.get_attribute('aria-expanded')
        return True if is_expanded == 'true' else False

    def expand_first_playlists(self):
        self.first_playlists.click()

    def click_on_first_track(self):
        """
        clicking on the first track
        """
        self.scroll_to_element(self._track)
        track = self.get_element(self._track)
        track.click()

    def get_current_track_state(self):
        """
        :return: True if track is selected else False
        """
        track = self.get_element(self._track)
        att = track.get_attribute('class')
        return True if 'selected' in att else False

    def click_next(self):
        self.scroll_to_element(self._next_btn)
        next_btn = self.get_element(self._next_btn)
        next_btn.click()
