import sys
import os
import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.test_data import USER_DATA
from utils.utility import Utility

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.mark.usefixtures("driver")
class TestLogout(Utility):
    def test_logout(self, driver):
        LoginPage.login_and_assert(driver, USER_DATA["valid"]["username"], USER_DATA["valid"]["password"])
        HomePage.logout_and_assert(driver)
        self.message_logging("Successfully logged out and verified that login button is visible")
