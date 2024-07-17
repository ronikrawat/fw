from pom.register import RegisterationPage


class Test_Register:
    def test_register(self, driver):
        registration_page = RegisterationPage(driver)
        registration_page.register("Male", "Steve", "Jobs", "steve.jobs@apple.com", "Password123")
