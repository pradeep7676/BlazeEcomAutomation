# E-commerce Application Test Suite

This project contains automated tests for the E-commerce website [DemoBlaze](https://www.demoblaze.com/). The tests are written in Python using Selenium, pytest, and pytest-html for report generation.

## Table of Contents

- [Setup](#setup)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Logs](#Logfile)
- [Reports](#reports)
- [Screenshots](#screenshots)
- [License](#license)

## Setup

### Prerequisites

- Python 3.x
- pip (Python package installer)
- WebDriver for your browser (e.g., ChromeDriver for Chrome, geckodriver for Firefox)

### Install Dependencies

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/pradeep7676/BlazeEcomAutomation.git
cd BlazeEcomAutomation

Install the required Python packages:
-pip install selenium pytest pytest-html

Setup WebDriver
Download the WebDriver for your browser:

ChromeDriver
GeckoDriver (for Firefox)
Ensure that the WebDriver executable is in your system's PATH or specify the path in your test configuration.


To run the tests with the default browser (Chrome):
python run_tests.py

Logs
Logs will be generated automatically in the logs folder. The log file (logfile.log) contains detailed information about the test execution, including debug and error messages, which can be helpful for troubleshooting and debugging.


Specific Browser
To run the tests with a specific browser (e.g., Firefox):
python run_tests.py firefox

Reports
Test reports will be generated automatically in the reports folder. The reports are in HTML format and provide a detailed overview of the test results.

Screenshots
If any test case fails, a screenshot will be generated automatically and saved in the screenshots folder. The filename will correspond to the test case name.

License
This project is licensed under the MIT License - see the LICENSE file for details.

This `README.md` provides a comprehensive guide to setting up, running, and contributing to the project. It also details the project structure and the purpose of each test case, ensuring clarity for any new users or contributors.
