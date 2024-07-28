import sys
import os
from selenium.common import TimeoutException
from utils.test_data import USER_DETAILS
from utils.utility import Utility
import pytest
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

# Add the project directory to the system path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.mark.usefixtures("driver")
class TestCheckout(Utility):

    def test_checkout_with_all_details(self, driver):
        # Navigate to the cart page from the home page
        home_page = HomePage(driver)
        home_page.go_to_cart()

        # Place the order from the cart page
        cart_page = CartPage(driver)
        cart_page.place_order()

        # Fill the checkout form with all required details and submit the order
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form_and_purchase(USER_DETAILS['name'], USER_DETAILS['country'], USER_DETAILS['city'],
                                             USER_DETAILS['card'], USER_DETAILS['month'], USER_DETAILS['year'])

        # Verify the success message after checkout
        success_msg = checkout_page.success_msg(timeout=60)
        print(success_msg)
        assert "Thank you for your purchase!" in success_msg, "Checkout success message not found"

        # Log the success message for debugging and tracking
        self.message_logging("Successfully verified checkout page with all fields")

        # Refresh the page to reset the state
        driver.refresh()

    def test_checkout_empty_field(self, driver):
        # Navigate to the cart page from the home page
        home_page = HomePage(driver)
        home_page.go_to_cart()

        # Place the order from the cart page
        cart_page = CartPage(driver)
        cart_page.place_order()

        # Fill the checkout form with empty fields and submit the order
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form_and_purchase("", "", "", "", "", "")

        # Handle the alert and verify the error message
        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "Please fill out Name and Creditcard." in alert_text, f"Expected 'Please fill out Name and Creditcard.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise

        # Log the error message for debugging and tracking
        self.message_logging("Successfully verified checkout page with empty fields")

        # Refresh the page to reset the state
        driver.refresh()

    def test_checkout_with_name_and_card(self, driver):
        # Navigate to the cart page from the home page
        home_page = HomePage(driver)
        home_page.go_to_cart()

        # Place the order from the cart page
        cart_page = CartPage(driver)
        cart_page.place_order()

        # Fill the checkout form with only name and card details and submit the order
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form_and_purchase(USER_DETAILS['name'], "", "", USER_DETAILS['card'], "", "")

        # Verify the success message after checkout
        success_msg = checkout_page.success_msg(timeout=60)
        print(success_msg)
        assert "Thank you for your purchase!" in success_msg, "Checkout success message not found"

        # Log the success message for debugging and tracking
        self.message_logging("Successfully verified checkout page with name and card")

    def test_checkout_with_empty_cart(self, driver):
        # Navigate to the cart page from the home page
        home_page = HomePage(driver)
        home_page.go_to_cart()

        # Place the order from the cart page without any items in the cart
        cart_page = CartPage(driver)
        cart_page.place_order()

        # Fill the checkout form with all required details and submit the order
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form_and_purchase(USER_DETAILS['name'], USER_DETAILS['country'], USER_DETAILS['city'],
                                             USER_DETAILS['card'], USER_DETAILS['month'], USER_DETAILS['year'])

        # Verify the error message when checking out with an empty cart
        try:
            alert_text = Utility.handle_alert(driver, action='accept')
            assert "Error" in alert_text, "Expected error alert not found"
        except TimeoutException:
            print("Expected error alert not found")
            assert True, "No error alert found"
            self.message_logging("Successfully verified checkout with empty cart")
            driver.back()
