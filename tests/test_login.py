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
    def test_login_with_valid_username_password(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_login()
        login_page = LoginPage(driver)
        login_page.login(USER_DATA["valid"]["username"], USER_DATA["valid"]["password"])
        user_profile_locator = (By.XPATH, "//a[contains(text(), 'Welcome')]")
        try:
            '''Waiting for the user profile element to be visible'''
            user_profile_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(user_profile_locator)
            )
            user_profile_text = user_profile_element.text
            assert USER_DATA["valid"]["username"] in user_profile_text
            print("Login successful")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        '''Add verification for successful login'''
        home_page.logout()
        self.message_logging("successfully login and verified the username")

    '''login with wrong username and password'''
    def test_login_with_wrong_username_password(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_login()
        login_page = LoginPage(driver)
        login_page.login(USER_DATA["invalid"]["username"], USER_DATA["invalid"]["password"])
        '''Adding verification for failed login'''
        alert_text = Utility.handle_alert(driver, action='accept')
        assert "User does not exist." in alert_text
        driver.refresh()
        self.message_logging("successfully verified by providing wrong username and password")

    '''login with wrong username'''
    def test_login_with_wrong_username(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_login()
        login_page = LoginPage(driver)
        login_page.login(USER_DATA["invalid"]["username"], USER_DATA["valid"]["password"])
        '''Adding verification for failed login'''
        alert_text = Utility.handle_alert(driver, action='accept')
        assert "User does not exist." in alert_text
        driver.refresh()
        self.message_logging("successfully verified by providing wrong username")

    '''login with wrong password'''
    def test_login_with_wrong_password(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_login()
        login_page = LoginPage(driver)
        login_page.login(USER_DATA["valid"]["username"], USER_DATA["invalid"]["password"])
        '''Adding verification for failed login'''
        alert_text = Utility.handle_alert(driver, action='accept')
        assert "Wrong password." in alert_text
        driver.refresh()
        self.message_logging("successfully verified by providing wrong password")

    '''login with empty fields'''
    def test_login_with_empty_fields(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_login()
        login_page = LoginPage(driver)
        login_page.login("", "")
        '''Adding verification for failed login'''
        alert_text = Utility.handle_alert(driver, action='accept')
        assert "Please fill out Username and Password." in alert_text
        self.message_logging("successfully verified by providing empty fields")
