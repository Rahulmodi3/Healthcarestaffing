import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """The BasePage class holds all common functionality across the website."""

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_visible(self, by_locator, timeout=20):
        visible_element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
        return visible_element

    def wait_for_element_to_be_invisible(self, by_locator, timeout=20):
        invisible_element = WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(by_locator))
        return invisible_element

    def wait_for_element_to_be_clickable(self, by_locator, timeout=20):
        clickable_element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(by_locator))
        return clickable_element

    def launch_url(self, url):
        self.driver.get(url)

    def maximize_window(self):
        self.driver.maximize_window()

    def do_click(self, by_locator):
        """ Performs click on web element """
        self.wait_for_element_to_be_clickable(by_locator).click()
        self.driver.implicitly_wait(20)

    def do_send_keys(self, by_locator, text: str):
        """ Performs send keys to web element """
        self.wait_for_element_to_be_clickable(by_locator).clear()
        self.wait_for_element_to_be_clickable(by_locator).send_keys(text)

    def get_element_text(self, by_locator):
        """ Get element text """
        element = self.wait_for_element_to_be_visible(by_locator)
        return element.text

    def element_is_enable(self, by_locator):
        """ Return element is enabled or not """
        element = self.wait_for_element_to_be_visible(by_locator)
        return bool(element.is_enabled())

    def element_is_visible(self, by_locator):
        """ Return element is visible or not """
        element = self.wait_for_element_to_be_visible(by_locator)
        return bool(element.is_displayed())

    def get_title(self):
        """Returns the title of the page"""
        return self.driver.title

    def get_all_elements(self, by_locator):
        element = self.driver.find_elements(*by_locator)
        return element
