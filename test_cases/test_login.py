from pages.home_page import HomePage
from test_base import BaseTest
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig


class Test_Login(BaseTest):
    LOGGER = LogGen.loggen()
    EMAIL = ReadConfig.get_user_email()
    PASSWORD = ReadConfig.get_password()

    def test_login(self):
        home = HomePage(self.driver)
        login = home.click_login()
        dashboard = login.login(self.EMAIL, self.PASSWORD)
        my_account = dashboard.is_visible_my_account()
        view_assignment = dashboard.is_visible_view_assignment()
        assert my_account == True
        assert view_assignment == True

    def test_validation_login(self):
        home = HomePage(self.driver)
        login = home.click_login()

        login.click_login()

        errors = login.get_errors_text()
        errors.__contains__("The email field is required.")
        errors.__contains__("The password field is required.")

    def test_sign_up_here_link_redirection(self):
        home = HomePage(self.driver)
        login = home.click_login()

        register = login.click_sign_up_here_link()

        get_header = register.get_header_text()
        assert get_header == ReadConfig.get_register_page_title()
        is_form_visible = register.is_visible_register_form()
        assert is_form_visible == True
        is_sign_in_link_visible = register.is_visible_sign_in_here_link()
        assert is_sign_in_link_visible == True