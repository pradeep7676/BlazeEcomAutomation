import sys
import os
import time

import pytest

from pages.home_page import HomePage
from pages.signup_page import SignupPage
from utils.test_data import USER_DATA
from utils.utility import Utility

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.mark.usefixtures("driver")
class TestSignup(Utility):


    def test_valid_signup(self, driver):
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
        self.message_logging("successfully signup with new username and password")

    '''negative testcase with existing username'''
    def test_existing_username(self, driver):
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
        self.message_logging("successfully signup")

    '''testcase with empty username'''
    def test_empty_username(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_signup()
        signup_page = SignupPage(driver)
        signup_page.signup("", USER_DATA["valid"]["password"])
        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "Please fill out Username and Password." in alert_text, f"Expected 'Please fill out Username and Password.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise  # Re-raise the exception to ensure the test is marked as failed
        self.message_logging("successfully verified with empty username and password fields")


    '''testcase with empty password'''
    def test_empty_password(self, driver):
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
        self.message_logging("successfully verified with empty username and password fields")


    '''testcase with empty fields'''
    def test_empty_fields(self, driver):
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
        self.message_logging("successfully verified with empty username and password fields")

    '''testcase with username and password containing special characters'''
    def test_username_password_with_special_characters(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_signup()
        signup_page = SignupPage(driver)
        signup_page.signup(USER_DATA["specialcha"]["spcecial_characters_username"], USER_DATA["specialcha"]["special_char_Password"])
        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "Sign up successful." in alert_text, f"Expected 'Sign up successful.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise
        self.message_logging("successfully signup with username and password special characters")

