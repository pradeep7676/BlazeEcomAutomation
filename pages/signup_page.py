from .base_page import BasePage
from selenium.webdriver.common.by import By


class SignupPage(BasePage):
    # Locators for various elements on the signup page
    USERNAME_INPUT = (By.ID, "sign-username")
    PASSWORD_INPUT = (By.ID, "sign-password")
    SIGNUP_BUTTON = (By.XPATH, "//button[contains(text(), 'Sign up')]")

    def signup(self, username, password):
        # Enter the username in the signup form
        self.send_keys(username, *self.USERNAME_INPUT)
        # Enter the password in the signup form
        self.send_keys(password, *self.PASSWORD_INPUT)
        # Click the signup button to submit the form
        self.click(*self.SIGNUP_BUTTON)
