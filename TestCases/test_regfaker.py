import time

import pytest
from Utilities.Faker import FakeData
from Utilities.ReadProperties import ReadConfig
from Utilities.CustomLogger import LogGen
from Pages.RegisterPage import  RegisterPage

class Test_004_Register:

    base_url = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    faker = FakeData()  # Create Faker instance

    @pytest.mark.sanity
    def test_register(self, setUp):
        self.logger.info("************* Test_002_Register Started *************")
        self.driver = setUp
        self.driver.get(self.base_url)

        self.lp = RegisterPage(self.driver)

        # Generate fake data using Faker class
        firstname = self.faker.get_first_name()
        lastname = self.faker.get_last_name()
        email = self.faker.get_email()
        telephone = self.faker.get_telephone()
        password = self.faker.get_password()

        self.logger.info(f"Using data: {firstname}, {lastname}, {email}, {telephone}, {password}")

        # Perform registration
        self.lp.clickMyAccountBtn()
        self.lp.clickResterBtn()
        self.lp.enterFirstName(firstname)
        self.lp.enterLastName(lastname)
        self.lp.enterEmail(email)
        self.lp.enterTelephone(telephone)
        self.lp.enterPassword(password)
        self.lp.enterRePassword(password)
        self.lp.selectRadiBtn()
        self.lp.selectPolicyCheckBox()
        time.sleep(2)
        self.lp.clickContinueBtn()

        act_title = self.driver.title
        assert act_title == "Your Account Has Been Created!"

        self.driver.close()
        self.logger.info("*************  Test_002_Log ended in****************")