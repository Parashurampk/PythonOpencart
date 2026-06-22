import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePageFooter:

    information_links_xpath = "//footer//div[contains(@class,'col-sm-3')][1]//a"
    customer_service_links_xpath = "//footer//div[contains(@class,'col-sm-3')][2]//a"
    extras_links_xpath = "//footer//div[contains(@class,'col-sm-3')][3]//a"
    my_account_links_xpath = "//footer//div[contains(@class,'col-sm-3')][4]//a"

    def __init__(self, driver):
        self.driver = driver

    def scrollToFooter(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, self.information_links_xpath)
            )
        )

    def getInformationLinks(self):
        elements = self.driver.find_elements(By.XPATH,
            self.information_links_xpath
        )
        return [element.text for element in elements]

    def getCustomerServiceLinks(self):
        elements = self.driver.find_elements(
            By.XPATH,
            self.customer_service_links_xpath
        )
        return [element.text for element in elements]

    def getExtrasLinks(self):
        elements = self.driver.find_elements(
            By.XPATH,
            self.extras_links_xpath
        )
        return [element.text for element in elements]

    def getMyAccountLinks(self):
        elements = self.driver.find_elements(
            By.XPATH,
            self.my_account_links_xpath
        )
        return [element.text for element in elements]