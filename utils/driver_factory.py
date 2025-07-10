from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def get_driver(browser="chrome"):
    if browser == "chrome":
        return webdriver.Chrome()
    elif browser == "firefox":
        return webdriver.Firefox()
    else:
        raise Exception(f"Unsupported browser: {browser}")
