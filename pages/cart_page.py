from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class CartPage(BasePage):
    # Locators for various elements on the cart page
    NEXT_BUTTON = (By.ID, "next2")
    SELECT_LAST_ITEM = (By.XPATH, "(//div[@class='card h-100'])[6]")
    ADD_TO_CART = (By.XPATH, "//a[@class='btn btn-success btn-lg']")
    CART_ITEM = (By.XPATH, "//tr[@class='success']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Place Order')]")
    CLICK_ON_CART = (By.XPATH, "//a[text()='Cart']")
    GET_ITEM_TEXT = (By.XPATH, "//a[text()='Delete']")

    def click_next_button(self):
        # Wait for the 'Next' button to be clickable and then click it
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NEXT_BUTTON)
        )
        element.click()

    def select_last_item(self):
        # Wait for the last product item to be present in the DOM
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SELECT_LAST_ITEM)
        )
        # Scroll the item into view to ensure it is visible
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # Click on the last item to select it
        element.click()

    def add_to_cart(self):
        # Wait for the 'Add to Cart' button to be clickable
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART)
        )
        # Scroll the button into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # Click on the 'Add to Cart' button
        element.click()

    def place_order(self):
        # Wait for the 'Place Order' button to be clickable
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PLACE_ORDER_BUTTON)
        )
        # Scroll the button into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # Click on the 'Place Order' button
        element.click()

    def click_on_cart(self):
        # Wait for the 'Cart' link to be clickable
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CLICK_ON_CART)
        )
        # Click on the 'Cart' link to navigate to the cart
        element.click()

    def verify_item(self):
        # Wait for the cart item text to be present in the DOM
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.GET_ITEM_TEXT)
        )
        # Return the text of the element, typically to verify if the item is present in the cart
        return element.text
