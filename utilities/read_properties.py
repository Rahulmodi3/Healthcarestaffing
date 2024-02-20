import configparser
from pathlib import Path


current_dir = Path(__file__)
project_name = 'EmPower(hshceu)'
root_dir = next(p for p in current_dir.parents if p.parts[-1] == project_name)
config_path = str(root_dir) + "\\configurations\\config.ini"

config = configparser.RawConfigParser()
config.read(config_path)
print(config_path)


class ReadConfig:

    @staticmethod
    def get_application_url():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def get_user_email():
        username = config.get('common info', 'userEmail')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def get_dashboard_title():
        title = config.get('common info', 'dashboardTitle')
        return title

    @staticmethod
    def get_register_page_title():
        title = config.get('register info', 'headerTitle')
        return title

    @staticmethod
    def get_register_password():
        password = config.get('register info', 'password')
        return password

    @staticmethod
    def get_register_thank_you_message():
        msg = config.get('register info', 'thankyouMessage')
        return msg

    @staticmethod
    def get_register_confirmation_message():
        msg = config.get('register info', 'confirmationMessage')
        return msg

    @staticmethod
    def get_login_page_title():
        title = config.get('login info', 'headerTitle')
        return title

    @staticmethod
    def get_login_text():
        txt = config.get('login info', 'loginText')
        return txt
