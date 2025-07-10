from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def is_backpack_in_cart(self):
        return self.get_text(self.ITEM_NAME) == "Sauce Labs Backpack"
