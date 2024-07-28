import sys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.home_page import HomePage
from utils.utility import Utility

# Add the project directory to the system path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.mark.usefixtures("driver")
class TestProductBrowsing(Utility):

    def test_product_display(self, driver):
        home_page = HomePage(driver)

        # Wait until the product container is visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(HomePage.PRODUCT_CONTAINER)
        )

        # Retrieve the product elements from the home page
        products = home_page.get_product_elements()

        # Assert that at least one product is displayed
        assert len(products) > 0, "No products are displayed on the homepage."

        # Assert that each product has a name, price, and image
        for product in products:
            name, price, image = home_page.get_product_details(product)
            assert name, "Product name is missing."
            assert price, "Product price is missing."
            assert image, "Product image is missing."

        # Log the success message
        self.message_logging("Verified products are correctly displayed")

    def test_product_categories(self, driver):
        home_page = HomePage(driver)

        # Get the list of categories from the home page
        categories = home_page.get_categories()

        # Assert that there are categories present
        assert len(categories) > 0, "No categories are present."

        # Iterate through each category and test navigation
        for category in categories:
            category_name = category.text
            print(f"Testing category: {category_name}")

            # Click on the category to navigate to it
            category.click()

            # Wait until the product container is visible after navigating to the category
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(HomePage.PRODUCT_CONTAINER)
            )

            # Navigate back to the home page
            driver.back()

            # Wait until all category links are visible again
            WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located(HomePage.CATEGORY_LINK)
            )

            # Assert that the category name is in the expected categories
            assert category_name in ["Phones", "Laptops", "Monitors"], f"Unexpected category '{category_name}' found."

        # Log the success message
        self.message_logging("Verified that product categories can be navigated successfully.")
