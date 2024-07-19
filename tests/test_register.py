from pytest import mark
from exel_lib import return_header, return_test_data


class Test_Register:
    header = return_header("smoke", "test_registration")
    data = return_test_data("smoke", "test_registration")

    @mark.parametrize(header, data)
    def test_register(self, pages, gender, fname, lname, email, password, confirmpassword):
        pages.homepage.click_register()
        pages.regpage.register(gender, fname, lname,
                               email, password, confirmpassword)
