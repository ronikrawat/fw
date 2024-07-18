from _lib import Selenium_Wrapper
from exel_lib import read_locators,add_elements

@add_elements("loginpage")
class LoginPage:
    #locator = read_locators("loginpage")

    def __init__(self, driver):
        self.driver = driver
        self.wrapper = Selenium_Wrapper(self.driver)

    def login(self, email, password):
        self.wrapper.send_text(self.txt_email, email)
        self.wrapper.send_text(self.txt_password, password)
        self.wrapper.click_element(self.btn_login)
