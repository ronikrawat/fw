from pom.register import RegisterationPage


class Test_Register:
    def test_register(self, pages):
        pages.homepage.click_register()
        pages.regpage.register("Male", "Steve", "Jobs", "steve.jobs@apple.com", "Password123")