from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[contains(text(), 'Add to cart')]")

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART_BUTTON)
