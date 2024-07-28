import sys
import os
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.confiq import Config

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="module")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        #chrome_options = ChromeOptions()
        #chrome_options.add_argument("--headless")
        #chrome_options.add_argument("--disable-gpu")
        service = Service(Config.CHROME_DRIVER)
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.binary_location = Config.FIREFOX_BINARY_PATH
        firefox_options.add_argument("--headless")
        service = FirefoxService(Config.GECKO_DRIVER)
        driver = webdriver.Firefox(service=service, options=firefox_options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    driver.get(Config.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def setup_method(driver):
    driver.get(Config.BASE_URL)

@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact(node, call, report):
    if report.failed:
        if hasattr(node, 'funcargs'):
            driver = node.funcargs.get('driver')
            if driver:
                screenshot_dir = Config.SCREESHOTS
                if not os.path.exists(screenshot_dir):
                    os.makedirs(screenshot_dir)
                screenshot_path = os.path.join(screenshot_dir, f"{node.name}.png")
                driver.save_screenshot(screenshot_path)
                print(f"Screenshot saved to {screenshot_path}")

@pytest.hookimpl(trylast=True)
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    failed_tests = terminalreporter.stats.get('failed', [])
    if failed_tests:
        terminalreporter.write_sep("=", "FAILED TESTS", red=True)
        for test in failed_tests:
            terminalreporter.write_line(f":: {test.nodeid}", red=True)
            if hasattr(test, 'longrepr'):
                longrepr = str(test.longrepr)
                terminalreporter.write_line(f"{longrepr}", red=True)

def pytest_runtest_logreport(report):
    if report.failed:
        print(f"\033[91mTest {report.nodeid} failed\033[0m")
