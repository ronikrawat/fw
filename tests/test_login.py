from pom.login import LoginPage


class Test_Login:
    def test_login(self, pages):
        pages.homepage.click_login()
        pages.loginpage.login("admin","password")