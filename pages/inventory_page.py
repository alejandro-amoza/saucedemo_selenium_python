from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.base_page import BasePage

class InventoryPage(BasePage):
    ADD_BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Agregar mochila Sauce Labs al carrito")
    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK_BTN)

    @allure.step("Ir al carrito desde el ícono superior")
    def go_to_cart(self):
        self.click(self.CART_ICON)
        WebDriverWait(self.driver, 10).until(EC.url_contains("cart.html"))
