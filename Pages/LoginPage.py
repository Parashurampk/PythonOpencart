from selenium.webdriver.common.by import By

class LoginPage:

    button_MyAccount_xpath = "//span[normalize-space()='My Account']"
    button_Login_xpath = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']"
    txt_emailAddress_xpath = "//input[@id='input-email']"
    txt_Password_xpath = "//input[@id='input-password']"
    btn_Login_xpath = "//input[@value='Login']"
    btn_Logout_xpath = "//a[@class='list-group-item'][normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def clickMyAccountBtn(self):
        self.driver.find_element(By.XPATH, self.button_MyAccount_xpath).click()

    def clickLoginBtn(self):
        self.driver.find_element(By.XPATH, self.button_Login_xpath).click()

    def setUsername(self, username):
        self.driver.find_element(By.XPATH, self.txt_emailAddress_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txt_Password_xpath).send_keys(password)

    def doLogin(self):
        self.driver.find_element(By.XPATH, self.btn_Login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.btn_Logout_xpath).click()
