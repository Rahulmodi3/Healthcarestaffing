from selenium.webdriver.common.by import By
from base_page import BasePage
from pages.dashboard_page import DashboardPage



class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_header_text(self) -> str:
        return self.get_element_text(self.Selectors.HEADER_TEXT)

    def get_login_text(self) -> str:
        return self.get_element_text(self.Selectors.LOGIN_TEXT)

    def set_email(self, username):
        self.do_send_keys(self.Selectors.TXT_EMAIL, username)

    def set_password(self, password):
        self.do_send_keys(self.Selectors.TXT_PASSWORD, password)

    def click_login(self):
        self.do_click(self.Selectors.BTN_LOGIN)

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login()
        return DashboardPage(self.driver)

    def is_visible_sign_up_here_link(self) -> bool:
        return self.element_is_visible(self.Selectors.LNK_SIGN_UP_HERE)

    def click_sign_up_here_link(self):
        self.do_click(self.Selectors.LNK_SIGN_UP_HERE)
        from pages.register_page import RegisterPage
        return RegisterPage(self.driver)

    def get_errors_text(self):
        errors_text = []
        error_elements = self.get_all_elements(self.Selectors.LBL_ERRORS)
        for error in error_elements:
            errors_text.append(error.text)
        return errors_text

    class Selectors:
        HEADER_TEXT = (By.TAG_NAME, "h1")
        LOGIN_TEXT = (By.XPATH, "//h1//following-sibling::p")
        TXT_EMAIL = (By.CSS_SELECTOR, "input[name='email']")
        TXT_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
        BTN_LOGIN = (By.XPATH, "//button[text()='Login']")
        LNK_FORGOT_PASSWORD = (By.LINK_TEXT, "Forgot your password?")
        CHK_REMEMBER_ME = (By.CSS_SELECTOR, "input[name='remember_me']")
        LNK_SIGN_UP_HERE = (By.LINK_TEXT, "Signup here")

        LBL_ERROR_HEADER = (By.CSS_SELECTOR, "div.alert-heading ")
        LBL_ERRORS = (By.CSS_SELECTOR, "div.alert-danger ul>li")


