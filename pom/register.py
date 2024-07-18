from _lib import Selenium_Wrapper
from exel_lib import read_locators


class RegisterationPage:
    locator = read_locators("registrationpage")
    def __init__(self, driver):
        self.driver = driver
        self.wrapper = Selenium_Wrapper(self.driver)

    def register(self, gender, fname, lname, email, password):
        if gender.upper() == "MALE":
            self.wrapper.click_element(self.locator.get("rdo_male"))
        elif gender.upper() == "FEMALE":
            self.wrapper.click_element(self.locator.get("rdo_female"))
        self.wrapper.send_text(self.locator.get("txt_fname"), fname)
        self.wrapper.send_text(self.locator.get("txt_lname"), lname)
        self.wrapper.send_text(self.locator.get("txt_email"), email)
        self.wrapper.send_text(self.locator.get("txt_password"), password)
        self.wrapper.send_text(self.locator.get("txt_confirmpassword"), password)
        self.wrapper.click_element(self.locator.get("btn_register"))
