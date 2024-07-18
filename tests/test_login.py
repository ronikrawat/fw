from pom.login import LoginPage


class Test_Login:
    def test_login(self, pages, _config):
        pages.homepage.click_login()
        pages.loginpage.login(_config.id,_config.password)