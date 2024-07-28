import sys
import os
import pytest

from pages.home_page import HomePage
from pages.signup_page import SignupPage
from utils.test_data import USER_DATA
from utils.utility import Utility

# Add the project directory to the system path for module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.mark.usefixtures("driver")
class TestSignup(Utility):

    def test_valid_signup(self, driver):
        """Test case for valid signup with new username and password."""
        home_page = HomePage(driver)
        home_page.go_to_signup()
        signup_page = SignupPage(driver)
        signup_page.signup(USER_DATA["valid"]["username"], USER_DATA["valid"]["password"])

        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "Sign up successful." in alert_text, f"Expected 'Sign up successful.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise
        self.message_logging("Successfully signed up with new username and password")

    def test_existing_username(self, driver):
        """Negative test case for signup with an existing username."""
        home_page = HomePage(driver)
        home_page.go_to_signup()
        signup_page = SignupPage(driver)
        signup_page.signup(USER_DATA["valid"]["username"], USER_DATA["valid"]["password"])

        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "This user already exist." in alert_text, f"Expected 'This user already exist.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise
        self.message_logging("Signup with existing username verified successfully")

    def test_empty_username(self, driver):
        """Test case for signup with an empty username."""
        home_page = HomePage(driver)
        home_page.go_to_signup()
        signup_page = SignupPage(driver)
        signup_page.signup("", USER_DATA["valid"]["password"])

        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "Please fill out Username and Password." in alert_text, f"Expected 'Please fill out Username and Password.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise
        self.message_logging("Verified signup with empty username and password fields")

    def test_empty_password(self, driver):
        """Test case for signup with an empty password."""
        home_page = HomePage(driver)
        home_page.go_to_signup()
        signup_page = SignupPage(driver)
        signup_page.signup(USER_DATA["valid"]["username"], "")

        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "Please fill out Username and Password." in alert_text, f"Expected 'Please fill out Username and Password.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise
        self.message_logging("Verified signup with empty password")

    def test_empty_fields(self, driver):
        """Test case for signup with both fields empty."""
        home_page = HomePage(driver)
        home_page.go_to_signup()
        signup_page = SignupPage(driver)
        signup_page.signup("", "")

        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "Please fill out Username and Password." in alert_text, f"Expected 'Please fill out Username and Password.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise
        self.message_logging("Verified signup with both username and password fields empty")

    def test_username_password_with_special_characters(self, driver):
        """Test case for signup with username and password containing special characters."""
        home_page = HomePage(driver)
        home_page.go_to_signup()
        signup_page = SignupPage(driver)
        signup_page.signup(USER_DATA["specialcha"]["spcecial_characters_username"],
                           USER_DATA["specialcha"]["special_char_Password"])

        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "Sign up successful." in alert_text, f"Expected 'Sign up successful.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise
        self.message_logging("Successfully signed up with username and password containing special characters")
