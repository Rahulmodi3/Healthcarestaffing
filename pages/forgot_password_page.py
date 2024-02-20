from selenium.webdriver.common.by import By
from base_page import BasePage


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    class Selectors:
        HEADER_TEXT = (By.TAG_NAME, "h1")
        FORGOT_PASSWORD_TEXT = (By.XPATH, "//h1//following-sibling::h5")
        LNK_BACK_TO_LOGIN = (By.LINK_TEXT, "Back to Login")
        TXT_EMAIL = (By.XPATH, "//input[@id='email']")
        BTN_PASSWORD_RESET = (By.XPATH, "//button[@type='submit']")
