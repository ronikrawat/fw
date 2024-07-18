from pytest import mark
header = "gender, fname, lname, email, password"
test_data = [("Male", "Steve", "Jobs", "steve.jobs@apple.com", "Password123"),
             ("Female", "Nicole", "Turner", "nicole.turner@apple.com", "Password123")
             ]
@mark.parametrize(header,test_data)
class Test_Register:
    def test_register(self, pages,gender, fname, lname, email, password):
        pages.homepage.click_register()
        pages.regpage.register(gender, fname, lname, email, password)