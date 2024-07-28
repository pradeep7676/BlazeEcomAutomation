import time

import pytest
from pages.cart_page import CartPage
from utils.utility import Utility


@pytest.mark.usefixtures("driver")
class TestCart(Utility):
    def test_add_product_to_cart(self, driver):
        # Instantiate the CartPage object
        cart_page = CartPage(driver)

        '''Navigating to the cart page and interact with it'''
        # Click the next button to navigate to the last page
        cart_page.click_next_button()
        # Log the action for debugging and tracking
        self.message_logging("Navigate to the last page by clicking next")
        # Select the last product on the page
        cart_page.select_last_item()
        # Log the action for debugging and tracking
        self.message_logging("selecting the last product")
        # Add the selected product to the cart
        cart_page.add_to_cart()
        # Log the action for debugging and tracking
        self.message_logging("added the product to the cart")

        '''Verify product is added to the cart'''
        # Handle the alert that appears after adding the product to the cart
        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            # Assert that the alert text contains "Product added"
            assert "Product added" in alert_text, f"Expected 'Product added' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise
        # Log the success message
        self.message_logging("successfully added product to cart")
        # Refresh the page
        driver.refresh()

    '''verifying item in cart '''

    def test_verifying_item_in_cart(self, driver):
        # Instantiate the CartPage object
        cart_page = CartPage(driver)
        # Click on the cart to view the items
        cart_page.click_on_cart()
        # Retrieve the text of the item in the cart
        item_text = cart_page.verify_item()
        print(item_text)
        # Assert that the item text is present
        assert item_text, "Item text is not present, verification failed."
        # Log the success message
        self.message_logging("successfully verified that added product present")
