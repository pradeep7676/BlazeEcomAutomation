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

    def test_signup_new_user(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_signup()
        signup_page = SignupPage(driver)
        signup_page.signup(USER_DATA["valid"]["username"], USER_DATA["valid"]["password"])
        alert_text = Utility.handle_alert(driver, action='accept')
        assert "Sign up successful." in alert_text
        self.message_logging("successfully signup with new username and password")
        driver.refresh()

    '''negative testcase with empty field'''
    def test_signup_negative(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_signup()
        signup_page = SignupPage(driver)
        signup_page.signup("", "")
        alert_text = Utility.handle_alert(driver, action='accept')
        assert "Please fill out Username and Password." in alert_text
        self.message_logging("successfully verified with empty username and password fields")
        driver.refresh()

    '''negative testcase with existing username'''
    def test_signup_using_existing_user(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_signup()
        signup_page = SignupPage(driver)
        signup_page.signup(USER_DATA["valid"]["username"], USER_DATA["valid"]["password"])
        alert_text = Utility.handle_alert(driver, action='accept')
        assert "This user already exist." in alert_text
        self.message_logging("successfully signup")
