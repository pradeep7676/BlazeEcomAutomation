from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    # Locator for the "Add to Cart" button on the product page
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[contains(text(), 'Add to cart')]")

    def add_to_cart(self):
        # Click on the "Add to Cart" button to add the product to the shopping cart
        self.click(*self.ADD_TO_CART_BUTTON)
