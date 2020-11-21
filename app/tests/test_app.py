import unittest

from selenium import webdriver
from flask_testing import LiveServerTestCase

from app import create_app
from app.tests.login_page.login_page import Login
from app.tests.main_page.main_page import MainPage
from app.tests.select_tracks_page.select_tracks_page import SelectTracks
from app.tests.fine_tune.fine_tune import FineTune
from app.tests.your_playlist.your_playlist import YourPlaylist

from secrets import SPOTIFY_USERNAME, SPOTIFY_PASSWORD

import multiprocessing


class TestApp(LiveServerTestCase, unittest.TestCase):
    multiprocessing.set_start_method("fork")

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config.update(LIVESERVER_PORT=8002)
        return app

    @classmethod
    def setUpClass(cls):
        cls.chrome_browser = webdriver.Chrome()

    def test_01_main_page(self):
        self.chrome_browser.get(self.get_server_url())
        main_page = MainPage(self.chrome_browser)
        title = main_page.get_main_page_title()
        main_page.click_login()
        self.assertEqual(title, 'Spotify Playlist Generator')

    def test_02_login(self):
        login = Login(self.chrome_browser)

        login.login(SPOTIFY_USERNAME, SPOTIFY_PASSWORD)
        playlist = login.get_playlists()
        self.assertIsNotNone(playlist)

    def test_03_select_tracks(self):
        select_tracks = SelectTracks(self.chrome_browser)

        # check the playlist can expand
        self.assertFalse(select_tracks.check_if_expanded())
        select_tracks.expand_first_playlists()
        self.assertTrue(select_tracks.check_if_expanded())

        # check that a track can be selected
        select_tracks.click_on_first_track()
        self.assertTrue(select_tracks.get_current_track_state())

        # check that the alert shows up when clicking next and no track is selected
        select_tracks.click_on_first_track()
        select_tracks.click_next_without_any_selection()
        alert_text = select_tracks.get_alert_text()
        self.assertEqual(alert_text, 'Please select at least 1 track')
        select_tracks.click_on_first_track()

        # Click next
        select_tracks.click_next()

    def test_04_fine_tune(self):
        fine_tune = FineTune(self.chrome_browser)
        fine_tune.move_sliders()
        slider_values = fine_tune.get_sliders_values()

        # check that the sliders actually changed
        self.assertEqual(slider_values, ['9', '7', '5', '3'])
        fine_tune.click_next()

    def test_05_your_playlist(self):
        your_playlist = YourPlaylist(self.chrome_browser)
        total_tracks = your_playlist.get_total_tracks_amount()

        # check that the created playlist contains 25 tracks
        self.assertEqual(total_tracks, 25)
        your_playlist.save_playlist()


if __name__ == '__main__':
    unittest.main()
