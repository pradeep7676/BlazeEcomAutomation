import inspect
import logging
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.confiq import Config
from selenium.webdriver.support import expected_conditions as EC


class Utility:
    def handle_alert(driver, action='accept', timeout=30):
        try:
            alert = WebDriverWait(driver, timeout).until(EC.alert_is_present())
            alert_text = alert.text
            print(alert_text)
            '''Perform the action based on the parameter'''
            if action == 'accept':
                alert.accept()
            elif action == 'dismiss':
                alert.dismiss()
            return alert_text
        except NoAlertPresentException:
            print("No alert present")
            return None

    def message_logging(self, message):
            loggername = inspect.stack()[1][3]
            logger = logging.getLogger(loggername)
            filehandler = logging.FileHandler(Config.LOGFILE)
            logger.addHandler(filehandler)
            formatter = logging.Formatter(" %(asctime)s : %(levelname)s : %(name)s : %(message)s")
            filehandler.setFormatter(formatter)
            logger.setLevel(logging.INFO)
            logger.info(message)






