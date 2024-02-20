from selenium.webdriver.common.by import By
from base_page import BasePage
from pages.login_page import LoginPage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_header_text(self) -> str:
        return self.get_element_text(self.Selectors.HEADER_TEXT)

    def is_visible_register_form(self) -> bool:
        return self.element_is_visible(self.Selectors.REGISTER_FORM)

    def click_terms_of_service(self):
        self.do_click(self.Selectors.CHK_TERM_OF_SERVICE)

    def click_sign_up(self):
        self.do_click(self.Selectors.BTN_SIGN_UP)

    def set_value(self, name, value):
        selector = self.Selectors().get_form_selector(name)
        self.do_send_keys(selector, value)

    def is_visible_sign_in_here_link(self) -> bool:
        return self.element_is_visible(self.Selectors.LNK_SIGN_IN_HERE)

    def get_thank_you_message(self):
        return self.get_element_text(self.Selectors.TXT_THANK_YOU)

    def get_confirm_message_after_register(self):
        return self.get_element_text(self.Selectors.VERIFY_REGISTER_MESSAGE)

    def get_error_validation(self, name):
        selector = self.Selectors().get_form_error_selector(name)
        return self.get_element_text(selector)

    def click_sign_in_here(self):
        self.do_click(self.Selectors.LNK_SIGN_IN_HERE)
        return LoginPage(self.driver)

    @staticmethod
    def expected_validation_error(name):
        return f"Enter your {name}"

    class Selectors:
        HEADER_TEXT = (By.TAG_NAME, "h1")
        REGISTER_FORM = (By.XPATH, "//form[@id='registerForm']")
        TXT_FIRST_NAME = (By.XPATH, "//input[@id='firstName']")
        TXT_LAST_NAME = (By.XPATH, "//input[@id='lastName']")
        TXT_EMAIL = (By.XPATH, "//input[@id='inputEmail']")
        TXT_PHONE = (By.XPATH, "//input[@id='Phone']")
        TXT_PASSWORD = (By.XPATH, "//input[@id='inputpassword']")
        TXT_CONFIRM_PASSWORD = (By.XPATH, "//input[@id='password_confirmation']")
        CHK_TERM_OF_SERVICE = (By.ID, "agree_terms_of_service")
        BTN_SIGN_UP = (By.XPATH, "//button[@type='submit']")
        LNK_SIGN_IN_HERE = (By.LINK_TEXT, "Sign in here")
        TXT_THANK_YOU = (By.XPATH, "//div[contains(@class,'text-center')]//h2")
        VERIFY_REGISTER_MESSAGE = (By.XPATH, "//div[contains(@class,'text-center')]//p")


        """ Validation selectors """
        LBL_ERROR_FIRST_NAME = (By.XPATH, "//label[@id='firstName-error']")
        LBL_ERROR_LAST_NAME = (By.XPATH, "//label[@id='lastName-error']")
        LBL_ERROR_EMAIL = (By.XPATH, "//label[@id='inputEmail-error']")
        LBL_ERROR_PHONE = (By.XPATH, "//label[@id='Phone-error']")
        LBL_ERROR_PASSWORD = (By.XPATH, "//label[@id='inputpassword-error']")
        LBL_ERROR_CONFIRM_PASSWORD = (By.XPATH, "//label[@id='password_confirmation-error']")
        LBL_ERROR_TERM_OF_SERVICE = (By.XPATH, "//label[@id='terms_of_service-error']")

        def get_form_selector(self, name):
            match name:
                case "firstname":
                    return self.TXT_FIRST_NAME
                case "lastname":
                    return self.TXT_LAST_NAME
                case "email":
                    return self.TXT_EMAIL
                case "phone":
                    return self.TXT_PHONE
                case "password":
                    return self.TXT_PASSWORD
                case "password_confirmation":
                    return self.TXT_CONFIRM_PASSWORD
                case _:
                    raise f"{name} is not found"

        def get_form_error_selector(self, name):
            match name:
                case "firstname":
                    return self.LBL_ERROR_FIRST_NAME
                case "lastname":
                    return self.LBL_ERROR_LAST_NAME
                case "email":
                    return self.LBL_ERROR_EMAIL
                case "phone":
                    return self.LBL_ERROR_PHONE
                case "password":
                    return self.LBL_ERROR_PASSWORD
                case "password_confirmation":
                    return self.LBL_ERROR_CONFIRM_PASSWORD
                case "terms_of_service":
                    return self.LBL_ERROR_TERM_OF_SERVICE
                case _:
                    raise f"{name} is not found"
