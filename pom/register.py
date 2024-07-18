from _lib import Selenium_Wrapper
from exel_lib import add_elements


@add_elements("registrationpage")
class RegisterationPage:
    # locator = read_locators("registrationpage")
    def __init__(self, driver):
        self.driver = driver
        self.wrapper = Selenium_Wrapper(self.driver)

    def register(self, gender, fname, lname, email, password):
        if gender.upper() == "MALE":
            self.wrapper.click_element(self.rdo_male)
        elif gender.upper() == "FEMALE":
            self.wrapper.click_element(self.rdo_female)
        self.wrapper.send_text(self.txt_fname, fname)
        self.wrapper.send_text(self.txt_lname, lname)
        self.wrapper.send_text(self.txt_email, email)
        self.wrapper.send_text(self.txt_password, password)
        self.wrapper.send_text(self.txt_confirmpassword, password)
        self.wrapper.click_element(self.btn_register)
