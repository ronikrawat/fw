from exel_lib import return_header, return_test_data
from pytest import mark


class Test_Login:
    headers = return_header("smoke", "test_login_positive")
    data = return_test_data("smoke", "test_login_positive")

    @mark.parametrize(headers, data)
    def test_login_positive(self, pages, email, password):
        pages.homepage.click_login()
        pages.loginpage.login(email, password)
