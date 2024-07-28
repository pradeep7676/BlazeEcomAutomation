import sys
import os
import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.test_data import USER_DATA
from utils.utility import Utility

# Add the project directory to the system path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.mark.usefixtures("driver")
class TestLogout(Utility):

    def test_logout(self, driver):
        # Perform login with valid user data
        LoginPage.login_and_assert(driver, USER_DATA["valid"]["username"], USER_DATA["valid"]["password"])

        # Perform logout and verify successful logout
        HomePage.logout_and_assert(driver)

        # Log the success message
        self.message_logging("Successfully logged out and verified that login button is visible")
