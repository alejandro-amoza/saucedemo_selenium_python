import csv
import os
import pytest
import allure
from pages.login_page import LoginPage

def get_test_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
    csv_path = os.path.join(base_dir, "test_data", "users.csv")
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

@allure.feature("Login")
@allure.story("Login con múltiples usuarios desde CSV")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("TC001")
@allure.title("Validar login con usuario: {user[username]}")
@pytest.mark.parametrize("user", get_test_data())
def test_login_varios_usuarios(driver, user):
    login_page = LoginPage(driver)
    login_page.login(user['username'], user['password'])
    if user['username'] == 'locked_out_user':
        assert "Epic sadface" in driver.page_source
    else:
        assert "inventory.html" in driver.current_url
