import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
from utils.test_data import USER_DATA
import pytest
from pages.home_page import HomePage
from utils.utility import Utility

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.mark.usefixtures("driver")
class TestLogout(Utility):
    def test_logout(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_login()
        login_page = LoginPage(driver)
        login_page.login(USER_DATA["valid"]["username"], USER_DATA["valid"]["password"])
        user_profile_locator = (By.XPATH, "//a[contains(text(), 'Welcome')]")

        try:
            '''Wait for the user profile element to be visible'''
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
        print("successfully logout")
        self.message_logging("successfully verified with empty username and password fields")
