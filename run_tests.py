import pytest
import sys

def run_tests():
    """
    Run pytest test suites with specified or default browser.

    This function constructs pytest arguments and runs the test suites,
    allowing the browser to be specified via command line arguments.
    """
    # Default to Chrome if no browser is specified
    browser_name = "chrome"

    # Check if a browser name is provided via command line arguments
    if len(sys.argv) > 1:
        browser_name = sys.argv[1]

    # Construct the pytest arguments including the browser name
    pytest_args = [
        "tests/test_signup.py",  # Path to the signup test suite
        "tests/test_login.py",  # Path to the login test suite
        "tests/test_product_browisng.py",  # Path to the product browsing test suite
        "tests/test_cart.py",  # Path to the cart test suite
        "tests/test_checkout.py",  # Path to the checkout test suite
        "tests/test_logout.py",  # Path to the logout test suite
        f"--browser_name={browser_name}",  # Pass the browser name to pytest
        "--html=reports/report.html",  # Specify the report file path
        "--self-contained-html",  # Include this option for a self-contained HTML report
    ]

    # Run pytest with the constructed arguments
    pytest.main(pytest_args)

if __name__ == "__main__":
    run_tests()
