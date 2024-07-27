from .base_page import BasePage
from selenium.webdriver.common.by import By


class SignupPage(BasePage):
    USERNAME_INPUT = (By.ID, "sign-username")
    PASSWORD_INPUT = (By.ID, "sign-password")
    SIGNUP_BUTTON = (By.XPATH, "//button[contains(text(), 'Sign up')]")

    def signup(self, username, password):
        self.send_keys(username, *self.USERNAME_INPUT)
        self.send_keys(password, *self.PASSWORD_INPUT)
        self.click(*self.SIGNUP_BUTTON)


