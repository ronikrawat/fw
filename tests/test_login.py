from pom.login import LoginPage


class Test_Login:
    def test_login(self, driver, _config):
        login_page = LoginPage(driver, _config)
        login_page.login()
