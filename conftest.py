import pytest
from utils.driver_factory import get_driver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use: chrome or firefox")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver = get_driver(browser)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()
