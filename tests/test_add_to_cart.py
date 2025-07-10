from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import allure

@allure.feature("Añadir producto a carrito")
@allure.story("Funcionamiento correcto de carrito")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("TC002")
@allure.title("Validar correcto funcionamiento del carrito")
def test_añadir_producto_a_carrito(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.login("standard_user", "secret_sauce")
    
    assert "inventory.html" in driver.current_url
    
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()
    
    assert "cart.html" in driver.current_url
    
    assert cart_page.is_backpack_in_cart()
