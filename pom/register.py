from _lib import Selenium_Wrapper
from pom.homepage import Homepage
class RegisterationPage:

    def __init__(self,driver):
        self.driver = driver
        self.wrapper = Selenium_Wrapper(self.driver)
        self.homepage = Homepage(self.driver)
    def register(self,gender,fname,lname,email,password):
        self.homepage.click_register()
        if gender.upper() == "MALE":
            self.wrapper.click_element(("id", "gender-male"))
        elif gender.upper() == "FEMALE":
            self.wrapper.click_element(("id", "gender-female"))
        self.wrapper.send_text(("id", "FirstName"), fname)
        self.wrapper.send_text(("id", "LastName"), lname)
        self.wrapper.send_text(("id", "Email"), email)
        self.wrapper.send_text(("id", "Password"), password)
        self.wrapper.send_text(("id", "ConfirmPassword"), password)
        self.wrapper.click_element(("id", "register-button"))