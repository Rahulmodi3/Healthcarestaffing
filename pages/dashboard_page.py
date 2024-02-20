from selenium.webdriver.common.by import By
from base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_header_text(self) -> str:
        return self.get_element_text(self.Selectors.HEADER_TEXT)

    def is_visible_my_account(self) -> bool:
        return self.element_is_visible(self.Selectors.HEADER_MY_ACCOUNT)

    def is_visible_view_assignment(self) -> bool:
        return self.element_is_visible(self.Selectors.BUTTON_VIEW_ASSIGNMENTS)

    class Selectors:
        HEADER_TEXT = (By.TAG_NAME, "h1")
        HEADER_MY_ACCOUNT = (By.LINK_TEXT, "My Account")
        BUTTON_VIEW_ASSIGNMENTS = (By.LINK_TEXT, "View Assignments")
