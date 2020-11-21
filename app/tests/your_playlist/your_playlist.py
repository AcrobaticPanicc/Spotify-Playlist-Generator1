from app.tests.utilities import selenium_utility


class YourPlaylist(selenium_utility.SeleniumUtility):
    _tracks = '//li[contains(@class, "track")]'
    _playlist_name_input = '//input[@id="playlist_name_input"]'
    _save_playlist_btn = '//button[@id="save-playlist-btn"]'

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def get_total_tracks_amount(self):
        tracks = self.get_elements(self._tracks)
        return len(tracks)

    def save_playlist(self):
        self.scroll_to_element(self._playlist_name_input)
        playlist_name_input = self.get_element(self._playlist_name_input)
        playlist_name_input.send_keys('Test Playlist1')
        self.get_element(self._save_playlist_btn).click()
