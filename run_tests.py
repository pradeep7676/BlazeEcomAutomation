import pytest
import sys

def run_tests():
    # Default to Chrome if no browser is specified
    browser_name = "chrome"

    # Check if a browser name is provided via command line arguments
    if len(sys.argv) > 1:
        browser_name = sys.argv[1]

    # Construct the pytest arguments including the browser name
    pytest_args = [
        "tests/test_signup.py",
        "tests/test_login.py",
        "tests/test_product_browisng.py",
        "tests/test_cart.py",
        "tests/test_checkout.py",
        "tests/test_logout.py",
        f"--browser_name={browser_name}",  # Pass the browser name to pytest
        "--html=reports/report.html",  # Specify the report file path
        "--self-contained-html",  # Include this option if you want a self-contained HTML report
    ]

    # Run pytest with the constructed arguments
    pytest.main(pytest_args)


if __name__ == "__main__":
    run_tests()
