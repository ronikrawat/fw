from _lib import Selenium_Wrapper
from pom.homepage import Homepage


class LoginPage:

    def __init__(self, driver, config):
        self.driver = driver
        self.wrapper = Selenium_Wrapper(self.driver)
        self.homepage = Homepage(self.driver)
        self.config = config

    def login(self):
        self.homepage.click_login()
        self.wrapper.send_text(("id", "Email"), self.config.id)
        self.wrapper.send_text(("id", "Password"), self.config.password)
        self.wrapper.click_element(("css selector", ".login-button"))