from selenium import webdriver
from pytest import fixture

from pom.homepage import Homepage
from pom.login import LoginPage
from pom.register import RegisterationPage


# env = "test"
# browser = "chrome"
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="test",
        dest="env",
        help="Pass the env: Test or Stage[env=test]")
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        dest="browser",
        help="Pass browser[browser=chrome]")
    parser.addoption("--headless", action="store_true", dest="headless")


class TestEnv:
    url = "https://demowebshop.tricentis.com/"
    id = "xyz@gmail.com"
    password = "Password@123"


class StageEnv:
    url = "https://demowebshop.tricentis.com/"
    id = "abc@gmail.com"
    password = "Password@123"


@fixture
def _config(request):
    env = request.config.getoption("env")
    if env.upper() == "TEST":
        return TestEnv()
    elif env.upper() == "STAGE":
        return StageEnv()
    else:
        raise Exception("Not a valid environment")


@fixture
def driver(request, _config):
    browser = request.config.option.browser
    headless = request.config.option.headless

    if browser.upper() == "CHROME":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        _driver = webdriver.Chrome(options=options)
    elif browser.upper() == "FIREFOX":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        _driver = webdriver.Firefox(options=options)
    elif browser.upper() == "EDGE":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument("--headless")
        _driver = webdriver.Edge(options=options)
    else:
        raise Exception("Not a valid web browser")
    _driver.get(_config.url)
    _driver.maximize_window()
    yield _driver
    _driver.close()


@fixture
def pages(driver):
    class Pages:
        loginpage = LoginPage(driver)
        homepage = Homepage(driver)
        regpage = RegisterationPage(driver)

    return Pages()
