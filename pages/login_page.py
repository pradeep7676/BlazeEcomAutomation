from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .home_page import HomePage


class LoginPage(BasePage):
    # Locators for various elements on the login page
    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Log in')]")
    USER_PROFILE = (By.XPATH, "//a[contains(text(), 'Welcome')]")

    def login(self, username, password):
        # Enter the username and password, then click the login button
        self.send_keys(username, *self.USERNAME_INPUT)
        self.send_keys(password, *self.PASSWORD_INPUT)
        self.click(*self.LOGIN_BUTTON)

    @staticmethod
    def login_and_assert(driver, username, password):
        # Navigate to the login page from the home page
        home_page = HomePage(driver)
        home_page.go_to_login()

        # Perform the login operation
        login_page = LoginPage(driver)
        login_page.login(username, password)

        user_profile_locator = LoginPage.USER_PROFILE

        try:
            # Wait for the user profile element to be visible
            user_profile_element = WebDriverWait(driver, 10).until(
                ec.visibility_of_element_located(user_profile_locator)
            )
            user_profile_text = user_profile_element.text

            # Assert that the username is present in the user profile text
            assert username in user_profile_text, f"Expected username '{username}' in user profile text, but got '{user_profile_text}'"
            print("Login successful")
        except Exception as e:
            # Print an error message if an exception occurs during login
            print(f"An unexpected error occurred during login: {e}")
            raise
