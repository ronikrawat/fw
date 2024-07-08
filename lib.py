from selenium.webdriver.support.select import Select


class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator: tuple[str, str]):
        self.driver.find_element(*locator).click()

    def enter_text(self, locator: tuple[str, str], value: str):
        self.driver.find_element(*locator).send_keys(value)

    def select_element(self, locator: tuple[str, str], value: str):
        listbox = self.driver.find_element(*locator)
        select = Select(listbox)
        select.select_by_visible_text(value)
