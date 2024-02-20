from pages.home_page import HomePage
from test_base import BaseTest
from utilities.custom_logger import LogGen
from utilities.generic_utilities import generate_random_email
from utilities.generic_utilities import generate_random_phone_number
from utilities.read_properties import ReadConfig


class Test_Register(BaseTest):
    LOGGER = LogGen.loggen()
    EXPECTED_HEADER_TEXT = ReadConfig.get_register_page_title()
    RANDOM_EMAIL = generate_random_email(8)
    RANDOM_PHONE = generate_random_phone_number()
    PASSWORD = ReadConfig.get_register_password()

    def test_new_register(self):
        home = HomePage(self.driver)
        register = home.click_free_trial()
        get_header = register.get_header_text()
        assert get_header == self.EXPECTED_HEADER_TEXT
        is_form_visible = register.is_visible_register_form()
        assert is_form_visible == True
        is_sign_in_link_visible = register.is_visible_sign_in_here_link()
        assert is_sign_in_link_visible == True

        # set value
        register.set_value("firstname", "test_firstname")
        register.set_value("lastname", "test_lastname")
        register.set_value("email", self.RANDOM_EMAIL)
        register.set_value("phone", self.RANDOM_PHONE)
        register.set_value("password", self.PASSWORD)
        register.set_value("password_confirmation", self.PASSWORD)
        register.click_terms_of_service()

        register.click_sign_up()

        thank_you_msg = register.get_thank_you_message()
        confirmation_message = register.get_confirm_message_after_register()
        assert thank_you_msg == ReadConfig.get_register_thank_you_message()
        assert confirmation_message == ReadConfig.get_register_confirmation_message()

    def test_validation_register(self):
        home = HomePage(self.driver)
        register = home.click_free_trial()

        register.click_sign_up()

        firstname_error = register.get_error_validation("firstname")
        lastname_error = register.get_error_validation("lastname")
        email_error = register.get_error_validation("email")
        phone_error = register.get_error_validation("phone")
        password_error = register.get_error_validation("password")
        password_confirmation_error = register.get_error_validation("password_confirmation")
        terms_of_service_error = register.get_error_validation("terms_of_service")

        assert firstname_error == register.expected_validation_error("first name")
        assert lastname_error == register.expected_validation_error("last name")
        assert email_error == register.expected_validation_error("email address")
        assert phone_error == register.expected_validation_error("phone number")
        assert password_error == register.expected_validation_error("password")
        assert password_confirmation_error == register.expected_validation_error("confirm password")
        assert terms_of_service_error == "Required agree to the terms of service."

    def test_sign_in_here_link_redirection(self):
        home = HomePage(self.driver)
        register = home.click_free_trial()

        login = register.click_sign_in_here()

        get_header = login.get_header_text()
        get_tex = login.get_login_text()
        assert get_header == ReadConfig.get_login_page_title()
        assert get_tex == ReadConfig.get_login_text()
        is_sign_up_link_visible = login.is_visible_sign_up_here_link()
        assert is_sign_up_link_visible == True

