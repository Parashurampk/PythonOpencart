import time

import pytest
from Pages.RegisterPage import RegisterPage
from Utilities.ReadProperties import ReadConfig
from Utilities.CustomLogger import LogGen
import time

class Test_003_Register:

    base_url = ReadConfig.getApplicationURL()
    firstname = "Ram"
    lastname = "Sam"
    email = "testwadli1gg2@gmail.com"
    telephone = 9902545256
    password = "test"
    RePassword = "test"

    logger = LogGen.loggen()
    @pytest.mark.sanity
    def test_resister(self, setUp):

        self.logger.info("*************  Test_002_Log started in****************")
        self.logger.info("*************  Verifying Registering Opencart  ****************")
        self.driver = setUp
        self.driver.get(self.base_url)

        self.lp = RegisterPage(self.driver)

        self.lp.clickMyAccountBtn()
        self.lp.clickResterBtn()

        self.lp.enterFirstName(self.firstname)
        self.lp.enterLastName(self.lastname)
        self.lp.enterEmail(self.email)
        self.lp.enterTelephone(self.telephone)
        self.lp.enterPassword(self.password)
        self.lp.enterRePassword(self.RePassword)

        self.lp.selectRadiBtn()
        self.lp.selectPolicyCheckBox()
        time.sleep(2)
        self.lp.clickContinueBtn()

        act_title = self.driver.title
        assert act_title == "Your Account Has Been Created!"

        self.driver.close()
        self.logger.info("*************  Test_002_Log ended in****************")
