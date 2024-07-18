from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


def _wait(func):
    def wrapper(*args, **kwargs):
        wait = WebDriverWait(args[0].driver, 10)
        v = visibility_of_element_located(args[1])
        wait.until(v)
        return func(*args, **kwargs)

    return wrapper


def __wait(cls):
    for key, value in cls.__dict__.items():
        if callable(value) and key != "__init__":
            setattr(cls, key, _wait(value))
    return cls


@__wait
class Selenium_Wrapper:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def send_text(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def select_element(self, locator, value):
        select = Select(self.driver.find_element(*locator))
        select.select_by_visible_text(value)
