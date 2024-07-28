from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    def find_element(self, *locator):
        # Wait for the element to be visible and return it
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def click(self, *locator):
        # Find the element and click it
        self.find_element(*locator).click()

    def send_keys(self, text, *locator):
        # Find the element and send the provided text to it
        self.find_element(*locator).send_keys(text)
