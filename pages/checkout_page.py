from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from .base_page import BasePage


class CheckoutPage(BasePage):
    # Locators for various elements on the checkout page
    NAME_INPUT = (By.ID, "name")
    COUNTRY_INPUT = (By.ID, "country")
    CITY_INPUT = (By.ID, "city")
    CREDIT_CARD_INPUT = (By.ID, "card")
    MONTH_INPUT = (By.ID, "month")
    YEAR_INPUT = (By.ID, "year")
    PURCHASE_BUTTON = (By.XPATH, "//button[contains(text(), 'Purchase')]")
    SUCCESS = (By.XPATH, "//div[@class='sweet-alert  showSweetAlert visible']")

    def fill_form_and_purchase(self, name, country, city, card, month, year):
        # Wait for the name input field to be visible and enter the provided name
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.NAME_INPUT)).send_keys(name)

        # Fill out the rest of the form fields with the provided data
        self.driver.find_element(*self.COUNTRY_INPUT).send_keys(country)
        self.driver.find_element(*self.CITY_INPUT).send_keys(city)
        self.driver.find_element(*self.CREDIT_CARD_INPUT).send_keys(card)
        self.driver.find_element(*self.MONTH_INPUT).send_keys(month)
        self.driver.find_element(*self.YEAR_INPUT).send_keys(year)

        # Wait for the 'Purchase' button to be clickable
        purchase_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.PURCHASE_BUTTON)
        )
        # Scroll the button into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", purchase_button)
        # Click on the 'Purchase' button
        purchase_button.click()

    def success_msg(self, timeout=30):
        try:
            # Wait for the success message to appear within the given timeout period
            element = WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located(self.SUCCESS)
            )
            # Return the text of the success message
            return element.text
        except TimeoutException:
            # Print an error message if the success message is not found within the timeout period
            print("Success message not found within the timeout period")
            return None
