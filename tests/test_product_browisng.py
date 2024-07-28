import sys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.home_page import HomePage
from utils.utility import Utility

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.mark.usefixtures("driver")
class TestProductBrowsing(Utility):
    def test_product_display(self, driver):
        home_page = HomePage(driver)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(HomePage.PRODUCT_CONTAINER)
        )
        products = home_page.get_product_elements()
        assert len(products) > 0, "No products are displayed on the homepage."
        '''asserting products displayed correctly'''
        for product in products:
            name, price, image = home_page.get_product_details(product)
            assert name, "Product name is missing."
            assert price, "Product price is missing."
            assert image, "Product image is missing."
        self.message_logging("verified products correctly displayed")

    def test_product_categories(self, driver):
        home_page = HomePage(driver)
        '''Get list of categories'''
        categories = home_page.get_categories()
        assert len(categories) > 0, "No categories are present."

        for category in categories:
            category_name = category.text
            print(f"Testing category: {category_name}")
            category.click()
            '''Wait for the page to load and products to be displayed'''
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(HomePage.PRODUCT_CONTAINER)
            )
            driver.back()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located(HomePage.CATEGORY_LINK)
            )
            assert category_name in "Phones, Laptops,Monitors"
            self.message_logging("Verify that product categories can be navigated successfully.")