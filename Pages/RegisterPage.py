from selenium.webdriver.common.by import By

class RegisterPage:
    link_MyAccount = "//span[normalize-space()='My Account']"
    link_Resister = "(//a[normalize-space()='Register'])[1]"
    txt_FirstName = "//input[@id='input-firstname']"
    txt_LastName = "//input[@id='input-lastname']"
    txt_email = "//input[@id='input-email']"
    txt_Telephone = "//input[@id='input-telephone']"
    txt_password1 = "//input[@id='input-password']"
    txt_rePassword = "//input[@id='input-confirm']"
    radio_Btn = "//input[@value='0']"
    policy_CheckBox = "//input[@name='agree']"
    Continue_ClickBtn = "(//input[@value='Continue'])[1]"
    Account_SuccessMsg = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver

    def clickMyAccountBtn(self):
        self.driver.find_element(By.XPATH, self.link_MyAccount).click()

    def clickResterBtn(self):
        self.driver.find_element(By.XPATH, self.link_Resister).click()

    def enterFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.txt_FirstName).send_keys(firstname)

    def enterLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.txt_LastName).send_keys(lastname)

    def enterEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email).send_keys(email)

    def enterTelephone(self, telephone):
        self.driver.find_element(By.XPATH, self.txt_Telephone).send_keys(telephone)

    def enterPassword(self, password):
        self.driver.find_element(By.XPATH, self.txt_password1).send_keys(password)

    def enterRePassword(self, RePassword):
        self.driver.find_element(By.XPATH, self.txt_rePassword).send_keys(RePassword)

    def selectRadiBtn(self):
        self.driver.find_element(By.XPATH, self.radio_Btn)

    def selectPolicyCheckBox(self):
        self.driver.find_element(By.XPATH, self.policy_CheckBox).click()

    def clickContinueBtn(self):
        self.driver.find_element(By.XPATH, self.Continue_ClickBtn).click()