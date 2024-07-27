from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Log in')]")
    USER_PROFILE = (By.XPATH, "//a[contains(text(), 'Welcome')]")

    def login(self, username, password):
        self.send_keys(username, *self.USERNAME_INPUT)
        self.send_keys(password, *self.PASSWORD_INPUT)
        self.click(*self.LOGIN_BUTTON)
