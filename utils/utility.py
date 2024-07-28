import inspect
import logging
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.confiq import Config


class Utility:
    @staticmethod
    def handle_alert(driver, action='accept', timeout=30):
        """
        Handle browser alert pop-ups.

        Args:
            driver (WebDriver): The web driver instance.
            action (str): The action to perform on the alert ('accept' or 'dismiss').
            timeout (int): The time to wait for the alert to be present.

        Returns:
            str: The text of the alert if present, otherwise None.
        """
        try:
            # Wait for the alert to be present within the given timeout
            alert = WebDriverWait(driver, timeout).until(EC.alert_is_present())
            alert_text = alert.text
            print(alert_text)

            # Perform the specified action on the alert
            if action == 'accept':
                alert.accept()
            elif action == 'dismiss':
                alert.dismiss()
            return alert_text
        except NoAlertPresentException:
            print("No alert present")
            return None

    def message_logging(self, message):
        """
        Log messages to a specified log file.

        Args:
            message (str): The message to log.
        """
        # Get the name of the calling function for contextual logging
        loggername = inspect.stack()[1][3]

        # Create a logger with the name of the calling function
        logger = logging.getLogger(loggername)

        # Set up file handler for logging to the specified log file
        filehandler = logging.FileHandler(Config.LOGFILE)
        logger.addHandler(filehandler)

        # Define the log message format
        formatter = logging.Formatter(" %(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)

        # Set the logging level to INFO
        logger.setLevel(logging.INFO)

        # Log the provided message
        logger.info(message)
