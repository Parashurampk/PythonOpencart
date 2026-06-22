from selenium.webdriver.common.by import By


class AddressMenuPage:

    AddressMenuList_xpath = "//div[@class='list-group']//a"

    def __init__(self, driver):
        self.driver = driver

    def clickMyAccountBtn(self):
        self.driver.find_element_by_xpath(self.AddressMenuList_xpath).click()

    def get_address_menu_count(self):
        menu_list = self.driver.find_elements( By.XPATH,self.AddressMenuList_xpath)
        return len(menu_list)

    def get_address_menu_texts(self):
        menu_list = self.driver.find_elements(By.XPATH,self.AddressMenuList_xpath)
        menu_texts = []

        for menu in menu_list:
            menu_texts.append(menu.text.strip())

        return menu_texts