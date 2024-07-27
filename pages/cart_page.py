# pages/cart_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class CartPage(BasePage):
    NEXT_BUTTON = (By.ID, "next2")
    SELECT_LAST_ITEM = (By.XPATH, "(//div[@class='card h-100'])[6]")
    ADD_TO_CART = (By.XPATH, "//a[@class='btn btn-success btn-lg']")
    CART_ITEM = (By.XPATH, "//tr[@class='success']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Place Order')]")
    CLICK_ON_CART = (By.XPATH, "//a[text()='Cart']")
    GET_ITEM_TEXT = (By.XPATH, "//a[text()='Delete']")

    def click_next_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NEXT_BUTTON)
        )
        element.click()

    def select_last_item(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SELECT_LAST_ITEM)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def add_to_cart(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def place_order(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PLACE_ORDER_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_on_cart(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CLICK_ON_CART)
        )
        element.click()

    def verify_item(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.GET_ITEM_TEXT)
        )
        return element.text
