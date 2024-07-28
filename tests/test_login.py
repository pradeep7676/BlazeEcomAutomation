import sys
import os
from utils.utility import Utility
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.test_data import USER_DATA

# Add the project directory to the system path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.mark.usefixtures("driver")
class TestLogin(Utility):

    def test_valid_login(self, driver):
        # Perform login with valid user data and verify success
        LoginPage.login_and_assert(driver, USER_DATA["valid"]["username"], USER_DATA["valid"]["password"])
        # Log the success message
        self.message_logging("Successfully logged in with valid users")
        # Refresh the page to reset the state
        driver.refresh()

    def test_invalid_username_password(self, driver):
        # Navigate to the login page from the home page
        home_page = HomePage(driver)
        home_page.go_to_login()

        # Perform login with invalid username and password
        login_page = LoginPage(driver)
        login_page.login(USER_DATA["invalid"]["username"], USER_DATA["invalid"]["password"])

        # Handle the alert and verify the error message
        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "User does not exist." in alert_text, f"Expected 'User does not exist.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise

        # Log the verification message
        self.message_logging("Successfully verified by providing invalid username and password")
        # Refresh the page to reset the state
        driver.refresh()

    def test_invalid_username(self, driver):
        # Navigate to the login page from the home page
        home_page = HomePage(driver)
        home_page.go_to_login()

        # Perform login with an invalid username and a valid password
        login_page = LoginPage(driver)
        login_page.login(USER_DATA["invalid"]["username"], USER_DATA["valid"]["password"])

        # Handle the alert and verify the error message
        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "User does not exist." in alert_text, f"Expected 'User does not exist.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise

        # Log the verification message
        self.message_logging("Successfully verified by providing invalid username")

    def test_invalid_password(self, driver):
        # Navigate to the login page from the home page
        home_page = HomePage(driver)
        home_page.go_to_login()

        # Perform login with a valid username and an invalid password
        login_page = LoginPage(driver)
        login_page.login(USER_DATA["valid"]["username"], USER_DATA["invalid"]["password"])

        # Handle the alert and verify the error message
        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "Wrong password." in alert_text, f"Expected 'Wrong password.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise

        # Log the verification message
        self.message_logging("Successfully verified by providing invalid password")

    def test_empty_username(self, driver):
        # Navigate to the login page from the home page
        home_page = HomePage(driver)
        home_page.go_to_login()

        # Perform login with an empty username and a valid password
        login_page = LoginPage(driver)
        login_page.login("", USER_DATA["valid"]["password"])

        # Handle the alert and verify the error message
        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "Please fill out Username and Password." in alert_text, f"Expected 'Please fill out Username and Password.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise

        # Log the verification message
        self.message_logging("Successfully verified by providing empty username")

    def test_empty_password(self, driver):
        # Navigate to the login page from the home page
        home_page = HomePage(driver)
        home_page.go_to_login()

        # Perform login with a valid username and an empty password
        login_page = LoginPage(driver)
        login_page.login(USER_DATA["valid"]["username"], "")

        # Handle the alert and verify the error message
        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "Please fill out Username and Password." in alert_text, f"Expected 'Please fill out Username and Password.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise

        # Log the verification message
        self.message_logging("Successfully verified by providing empty password")
        # Refresh the page to reset the state
        driver.refresh()

    def test_empty_username_password(self, driver):
        # Navigate to the login page from the home page
        home_page = HomePage(driver)
        home_page.go_to_login()

        # Perform login with empty username and password fields
        login_page = LoginPage(driver)
        login_page.login("", "")

        # Handle the alert and verify the error message
        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "Please fill out Username and Password." in alert_text, f"Expected 'Please fill out Username and Password.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise

        # Log the verification message
        self.message_logging("Successfully verified by providing empty fields")
