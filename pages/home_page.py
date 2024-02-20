from selenium.webdriver.common.by import By
from base_page import BasePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_free_trial(self) -> RegisterPage:
        self.do_click(self.Selectors.BTN_FREE_TRIAL)
        return RegisterPage(self.driver)

    def click_login(self) -> LoginPage:
        self.do_click(self.Selectors.HEADER_LOGIN)
        return LoginPage(self.driver)

    class Selectors:
        BTN_FREE_TRIAL = (By.LINK_TEXT, "Free Trial")
        HEADER_LOGIN = (By.LINK_TEXT, "Login")
