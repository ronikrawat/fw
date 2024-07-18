from _lib import Selenium_Wrapper
from exel_lib import read_locators

class Homepage:
    locator = read_locators("homepage")
    def __init__(self, driver):
        self.driver = driver
        self.wrapper = Selenium_Wrapper(self.driver)

    def click_login(self):
        self.wrapper.click_element(self.locator.get("lnk_login"))

    def click_register(self):
        self.wrapper.click_element(self.locator.get("lnk_register"))