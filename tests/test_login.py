import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.utility import Utility
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.test_data import USER_DATA

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.mark.usefixtures("driver")
class TestLogin(Utility):
    def test_valid_login(self, driver):
        LoginPage.login_and_assert(driver, USER_DATA["valid"]["username"], USER_DATA["valid"]["password"])
        self.message_logging("successfully logged in with valid users")
        driver.refresh()

    def test_invalid_username_password(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_login()
        login_page = LoginPage(driver)
        login_page.login(USER_DATA["invalid"]["username"], USER_DATA["invalid"]["password"])
        '''Adding verification for failed login'''
        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "User does not exist." in alert_text, f"User does not exist.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise
        self.message_logging("successfully verified by providing invalid username and password")
        driver.refresh()

    '''login with wrong username'''
    def test_invalid_username(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_login()
        login_page = LoginPage(driver)
        login_page.login(USER_DATA["invalid"]["username"], USER_DATA["valid"]["password"])
        '''Adding verification for failed login'''
        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "User does not exist." in alert_text, f"User does not exist.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise
        self.message_logging("successfully verified by providing invalid username")

    '''login with wrong password'''
    def test_invalid_password(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_login()
        login_page = LoginPage(driver)
        login_page.login(USER_DATA["valid"]["username"], USER_DATA["invalid"]["password"])
        '''Adding verification for failed login'''
        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "Wrong password." in alert_text, f"Expected 'Wrong password.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise
        self.message_logging("successfully verified by providing invalid password")

    '''login with empty username'''
    def test_empty_username(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_login()
        login_page = LoginPage(driver)
        login_page.login("", USER_DATA["valid"]["password"])
        '''Adding verification for failed login'''
        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "Please fill out Username and Password." in alert_text, f"Expected 'Please fill out Username and Password.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise
        self.message_logging("successfully verified by providing empty username")

    '''login with empty password'''
    def test_empty_password(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_login()
        login_page = LoginPage(driver)
        login_page.login(USER_DATA["valid"]["username"], "")
        '''Adding verification for failed login'''
        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "Please fill out Username and Password." in alert_text, f"Expected 'Please fill out Username and Password.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise
        self.message_logging("successfully verified by providing empty password")
        driver.refresh()

    '''login with empty fields'''
    def test_empty_username_password(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_login()
        login_page = LoginPage(driver)
        login_page.login("", "")
        '''Adding verification for failed login'''
        alert_text = Utility.handle_alert(driver, action='accept')
        try:
            assert "Please fill out Username and Password." in alert_text, f"Expected 'Please fill out Username and Password.' in alert text, but got '{alert_text}'"
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise
        self.message_logging("successfully verified by providing empty fields")
