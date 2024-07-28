import sys
import os
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
        assert "Sign up successful." in alert_text
        self.message_logging("successfully signup with new username and password")
        driver.refresh()

    '''negative testcase with existing username'''
    def test_existing_username(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_signup()
        signup_page = SignupPage(driver)
        signup_page.signup(USER_DATA["valid"]["username"], USER_DATA["valid"]["password"])
        alert_text = Utility.handle_alert(driver, action='accept')
        assert "This user already exist." in alert_text
        self.message_logging("successfully signup")
        driver.refresh()
    '''testcase with empty username'''

    def test_empty_username(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_signup()
        signup_page = SignupPage(driver)
        signup_page.signup("", USER_DATA["valid"]["password"])
        alert_text = Utility.handle_alert(driver, action='accept')
        assert "Please fill out Username and Password." in alert_text
        self.message_logging("successfully verified with empty username and password fields")
        driver.refresh()

    '''testcase with empty password'''

    def test_empty_password(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_signup()
        signup_page = SignupPage(driver)
        signup_page.signup(USER_DATA["valid"]["username"], "")
        alert_text = Utility.handle_alert(driver, action='accept')
        assert "Please fill out Username and Password." in alert_text
        self.message_logging("successfully verified with empty username and password fields")
        driver.refresh()

    '''testcase with empty fields'''

    def test_empty_fields(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_signup()
        signup_page = SignupPage(driver)
        signup_page.signup("", "")
        alert_text = Utility.handle_alert(driver, action='accept')
        assert "Please fill out Username and Password." in alert_text
        self.message_logging("successfully verified with empty username and password fields")
        driver.refresh()

    def test_username_password_with_special_characters(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_signup()
        signup_page = SignupPage(driver)
        signup_page.signup(USER_DATA["specialcha"]["spcecial_characters_username"], USER_DATA["specialcha"]["special_char_Password"])
        alert_text = Utility.handle_alert(driver, action='accept')
        assert "Sign up successful." in alert_text
        self.message_logging("successfully signup  with username and password special characters")
        driver.refresh()





