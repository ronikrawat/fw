from _lib import Selenium_Wrapper
from exel_lib import add_elements


@add_elements("homepage")
class Homepage:
    # locator = read_locators("homepage")
    def __init__(self, driver):
        self.driver = driver
        self.wrapper = Selenium_Wrapper(self.driver)

    def click_login(self):
        self.wrapper.click_element(self.lnk_login)

    def click_register(self):
        self.wrapper.click_element(self.lnk_register)
