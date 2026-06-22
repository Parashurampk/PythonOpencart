import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from pytest_metadata.plugin import metadata_key

#==============================Command Line Option=========================
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser name: chrome or firefox"
    )

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#==========================Driver Setup=======================================
@pytest.fixture()
def setUp(browser):

    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")

    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")

    else:
        raise Exception(f"Unsupported Browser: {browser}")

    driver.maximize_window()

    yield driver

    driver.quit()

#================ HTML Report Metadata============================
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "OpenCartAutomation"
    config.stash[metadata_key]["Tester"] = "Parashuram"


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#================================ Screenshot on Failure=================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver: WebDriver = item.funcargs.get("setUp")
        if driver is not None:
            try:
                screenshot_dir = os.path.join( os.getcwd(),"Screenshots")
                os.makedirs(screenshot_dir, exist_ok=True)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

                screenshot_file = os.path.join(screenshot_dir,f"{item.name}_{timestamp}.png")

                if driver.session_id:
                    driver.save_screenshot(screenshot_file)
                    print(f"\nScreenshot saved: {screenshot_file}" )

            except Exception as e:
                print(f"\nUnable to capture screenshot: {e}")