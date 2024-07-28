import time

import pytest
from pages.cart_page import CartPage
from utils.utility import Utility


@pytest.mark.usefixtures("driver")
class TestCart(Utility):
    def test_add_product_to_cart(self, driver):
        # home_page = HomePage(driver)
        cart_page = CartPage(driver)

        '''Navigating to the cart page and interact with it'''
        cart_page.click_next_button()
        #time.sleep(1)
        self.message_logging("Navigate to the last page by clicking next")
        cart_page.select_last_item()
        #time.sleep(1)
        self.message_logging("selecting the last product")
        cart_page.add_to_cart()
        #time.sleep(1)
        self.message_logging("added the product to the cart")
        '''Verify product is added to the cart'''
        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "Product added" in alert_text, f"Expected 'Product added' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise
        assert "Product added" in alert_text
        self.message_logging("successfully added product to cart")
        driver.refresh()

    '''verifying item in cart '''

    def test_verifying_item_in_cart(self, driver):
        cart_page = CartPage(driver)
        cart_page.click_on_cart()
        #time.sleep(1)
        item_text = cart_page.verify_item()
        print(item_text)
        assert item_text, "Item text is not present, verification failed."
        self.message_logging("successfully verified that added product present in cart")

