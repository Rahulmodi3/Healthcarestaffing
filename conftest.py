from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.selenium_manager import SeleniumManager
import pytest

import logging as logger
from utilities.read_properties import ReadConfig



@pytest.fixture()
def setup(browser, headless, request):
    """
        Setup and Teardown browser.
        :param request:
        :param headless:
        :param browser:
        """
    global driver

    if browser == "chrome":
        chrome_option = webdriver.ChromeOptions()
        chrome_option.set_capability("browserName", "chrome")
        chrome_option.add_argument('--incognito')
        SeleniumManager().driver_location(chrome_option)

        if headless == "true":
            chrome_option.add_argument('--headless')
            chrome_option.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=chrome_option)
        request.cls.driver = driver
        logger.info("============================ launching Chrome Browser ============================")

    elif browser == "firefox":
        # SeleniumManager().driver_location('firefox')
        firefox_option = Options()
        firefox_option.set_capability("browserName", "firefox")
        if headless == "true":
            firefox_option.headless = True
            firefox_option.add_argument("--width=1920")
            firefox_option.add_argument("--height=1080")

        driver = webdriver.Firefox(options=firefox_option)
        request.cls.driver = driver
        logger.info(" ============================ launching FireFox Browser ============================")

    driver.get(ReadConfig.get_application_url())
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption('--browser_name', action="store", default="chrome", help='to run on specific browser')
    parser.addoption('--headless', action="store", default="false", help='to run on headless browser')


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser_name")


@pytest.fixture()
def headless(request):  # This will return the headless browser value to setup method
    return request.config.getoption("--headless")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')

        if (report.skipped and xfail) or (report.failed and not xfail):
            #file_name = report.nodeid.replace("::", "_") + ".png"
            screenshot = driver.get_screenshot_as_base64()
            extra.append(pytest_html.extras.image(screenshot, ''))
            # attached failure screenshot to allure report

        report.extra = extra
