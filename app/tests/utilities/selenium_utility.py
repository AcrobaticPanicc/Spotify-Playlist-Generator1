import logging
from pathlib import Path
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from time import sleep, strftime, localtime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from app.tests.utilities import logger


class SeleniumUtility:
    """
    This utilitie is used to make it easier to use Selenium
    """

    log = logger.Logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    @staticmethod
    def _get_by_type(locator_type):
        """Returning the By type. xpath -> By.XPATH"""
        return getattr(By, locator_type.upper())

    def send_key_command(self, element, key):
        """Sending key commands to a pre-found element. Keys.RETURN"""
        try:
            element.send_keys(getattr(Keys, key.upper()))
            self.log.info(f'Key: {key} sent to element: {element}')

        except AttributeError as e:
            print(e)
            self.log.info(f'Could not send keys to {element}')

    def take_screenshot(self, sleep_time=0):
        sleep(sleep_time)
        Path("screenshots").mkdir(exist_ok=True)
        t = localtime()
        current_time = str(strftime("%H:%M:%S", t))
        file_name = ''.join([current_time, '.png'])
        screenshot_directory = "screenshots"
        destination_file = '/'.join([screenshot_directory, file_name])
        self.driver.save_screenshot(destination_file)
        self.log.info(f'screenshot saved to {destination_file}')

    def get_element(self, locator, locator_type='xpath'):
        """Return found element"""
        by_type = self._get_by_type(locator_type)

        try:
            element = self.driver.find_element(by_type, locator)
            self.log.info(f'Element found. Locator: {locator}, Loctor type: {locator_type}')
            return element

        except NoSuchElementException as e:
            print(e)
            self.log.info(f'Element not found. Locator: {locator}, Loctor type: {locator_type}')

        except Exception as e:
            print(e)
            self.log.info(f'Error while locating {locator}. {e}')

    def get_elements(self, locator, locator_type='xpath'):
        """Return matching elements"""
        by_type = self._get_by_type(locator_type)
        try:
            elements = self.driver.find_elements(by_type, locator)
            return elements

        except NoSuchElementException as e:
            print(e)
            self.log.info(f'Element not found. Locator: {locator}, Loctor type: {locator_type}')

        except Exception as e:
            print(e)
            self.log.info(f'Error while locating {locator}. {e}')

    def scroll_to_element(self, locator, locator_type='xpath'):
        """Scroll to matching element"""
        element = self.get_element(locator, locator_type)
        if element:
            self.actions.move_to_element(element).perform()

    def deselct_dropdown(self, locator, locator_type='xpath'):
        """deselect all options from that SELECT on the page"""
        select = Select(self.get_element(locator, locator_type))
        select.deselect_all()

    def dropdown_select(self,
                        locator,
                        locator_type,
                        by_index=False,
                        by_visible_text=False,
                        by_value=False):

        select = Select(self.get_element(locator, locator_type))
        if by_index:
            select.select_by_index(by_index)
        elif by_visible_text:
            select.select_by_visible_text(by_visible_text)
        elif by_value:
            select.select_by_value(by_value)

    def wait_for_element(self, locator,
                         locator_type='xpath',
                         timeout=10,
                         poll_frequency=0.5):
        """Wait to presence of an element"""
        try:
            by_type = self._get_by_type(locator_type)

            wait = WebDriverWait(self.driver,
                                 timeout,
                                 poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])

            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            self.log.info(f'Element found. Locator: {locator}, Loctor type: {locator_type}')
            return element

        except TimeoutException:
            self.log.info('time out exception')

        except InvalidArgumentException:
            self.log.info(f'Element not found. Locator: {locator}, Loctor type: {locator_type}')
