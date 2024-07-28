from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class HomePage(BasePage):
    SIGNUP_LINK = (By.ID, "signin2")
    LOGIN_LINK = (By.ID, "login2")
    LOGOUT_LINK = (By.ID, "logout2")
    PRODUCT_LINK = (By.XPATH, "//a[@class='hrefch']")
    CATEGORY_LINK = (By.XPATH, "//a[@id='itemc']")
    PRODUCT_CONTAINER = (By.CSS_SELECTOR, ".card")  # Adjust this selector based on actual HTML
    PRODUCT_NAME = (By.CSS_SELECTOR, ".hrefch")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='card h-100']/div/h5")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, ".card-img-top ")
    CART_BUTTON = (By.XPATH, "//a[text()='Cart']")

    def go_to_signup(self):
        self.click(*self.SIGNUP_LINK)

    def go_to_login(self):
        self.click(*self.LOGIN_LINK)

    def logout(self):
        self.click(*self.LOGOUT_LINK)

    def get_categories(self):
        return self.driver.find_elements(*self.CATEGORY_LINK)

    def get_product_elements(self):
        return self.driver.find_elements(*self.PRODUCT_CONTAINER)

    def get_product_details(self, product_element):
        name = product_element.find_element(*self.PRODUCT_NAME).text
        price = product_element.find_element(*self.PRODUCT_PRICE).text
        image = product_element.find_element(*self.PRODUCT_IMAGE).get_attribute('src')
        return name, price, image

    def select_product(self, product_name):
        products = self.driver.find_elements(*self.PRODUCT_LINK)
        for product in products:
            if product.text == product_name:
                product.click()
                break

    def is_login_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(*self.LOGIN_LINK)
            )
            return True
        except:
            return False

    def go_to_cart(self):
        element = self.driver.find_element(*self.CART_BUTTON)
        element.click()

    def logout_and_assert(driver):
        home_page = HomePage(driver)
        home_page.logout()

        login_link_locator = HomePage.LOGIN_LINK

        try:
            WebDriverWait(driver, 10).until(
                ec.visibility_of_element_located(login_link_locator)
            )
            assert driver.find_element(
                *login_link_locator).is_displayed(), "Logout failed: login link is not visible"
            print("Logout successful")
        except Exception as e:
            print(f"An unexpected error occurred during logout: {e}")
            raise