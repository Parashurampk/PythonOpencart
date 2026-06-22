from selenium.webdriver.common.by import By

class HomePage:

    featured_products_xpath = "//div[contains(@class,'product-thumb')]//h4/a"
    menu_tabs_xpath = "//ul[@class='nav navbar-nav']/li/a"

    def __init__(self, driver):
        self.driver = driver

    def getFeaturedProducts(self):
        products = self.driver.find_elements(By.XPATH, self.featured_products_xpath)
        print("Total Products Found:", len(products))
        for product in products:
            print(product.text)
        return [product.text for product in products]

    def getMenuTabs(self):
        menus = self.driver.find_elements(By.XPATH,self.menu_tabs_xpath)
        menu_list = []
        for menu in menus:
            menu_list.append(menu.text)
        return menu_list