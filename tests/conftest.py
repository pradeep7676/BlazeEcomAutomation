import sys
import os
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.confiq import Config

# Add the parent directory to sys.path to allow importing from utils
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def pytest_addoption(parser):
    # Adding a command-line option for selecting the browser
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="module")
def driver(request):
    # Fixture to initialize the WebDriver based on the selected browser
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        # Initialize Chrome WebDriver
        # Uncomment below lines for headless mode
        # chrome_options = ChromeOptions()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")
        service = Service(Config.CHROME_DRIVER)
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        # Initialize Firefox WebDriver
        firefox_options = FirefoxOptions()
        firefox_options.binary_location = Config.FIREFOX_BINARY_PATH
        firefox_options.add_argument("--headless")
        service = FirefoxService(Config.GECKO_DRIVER)
        driver = webdriver.Firefox(service=service, options=firefox_options)
    else:
        # Raise an error if the specified browser is not supported
        raise ValueError(f"Unsupported browser: {browser_name}")
    # Navigate to the base URL and maximize the window
    driver.get(Config.BASE_URL)
    driver.maximize_window()
    yield driver
    # Quit the WebDriver after the test module completes
    driver.quit()


@pytest.fixture(autouse=True)
def setup_method(driver):
    # Fixture to navigate to the base URL before each test
    driver.get(Config.BASE_URL)


@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact(node, call, report):
    # Hook to capture screenshots on test failure
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
    # Hook to print a summary of failed tests at the end of the test run
    failed_tests = terminalreporter.stats.get('failed', [])
    if failed_tests:
        terminalreporter.write_sep("=", "FAILED TESTS", red=True)
        for test in failed_tests:
            terminalreporter.write_line(f":: {test.nodeid}", red=True)
            if hasattr(test, 'longrepr'):
                longrepr = str(test.longrepr)
                terminalreporter.write_line(f"{longrepr}", red=True)


def pytest_runtest_logreport(report):
    # Hook to print a message to the console when a test fails
    if report.failed:
        print(f"\033[91mTest {report.nodeid} failed\033[0m")
