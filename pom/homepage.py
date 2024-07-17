from _lib import Selenium_Wrapper


class Homepage:

    def __init__(self, driver):
        self.driver = driver
        self.wrapper = Selenium_Wrapper(self.driver)

    def click_login(self):
        self.wrapper.click_element(("link text", "Log in"))

    def click_register(self):
        self.wrapper.click_element(("link text", "Register"))