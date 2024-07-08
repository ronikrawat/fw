from selenium.webdriver.chrome.webdriver import WebDriver
from lib import SeleniumWrapper
driver = WebDriver()
driver.implicitly_wait(3)
driver.get("https://demowebshop.tricentis.com/")


wrapper = SeleniumWrapper(driver)


# driver.find_element("link text", "Register").click()
wrapper.click_element(("link text", "Register"))

# driver.find_element("id", "gender-male").click()
wrapper.click_element(("id", "gender-male"))

# driver.find_element("id", "FirstName").send_keys("hello")
wrapper.enter_text(("id", "FirstName"),"hello")

# driver.find_element("id", "LastName").send_keys("world")
wrapper.enter_text(("id", "LastName"),"world")

# driver.find_element("id", "Email").send_keys("hello.world@gmail.com")
wrapper.enter_text(("id", "Email"),"hello.world@gmail.com")

# driver.find_element("id", "Password").send_keys("ConfirmPassword")
wrapper.enter_text(("id", "Password"),"Password123")

# driver.find_element("id", "ConfirmPassword").send_keys("ConfirmPassword")
wrapper.enter_text(("id", "ConfirmPassword"),"Password123")

# driver.find_element("id", "register-button").click()
wrapper.click_element(("id", "register-button"))
