import time

import pytest
from Pages.RegisterPage import RegisterPage
from Utilities.ReadProperties import ReadConfig
from Utilities.CustomLogger import LogGen
from Utilities.DBConnection import DBConnection
import time

class Test_003_Register:

    base_url = ReadConfig.getApplicationURL()
    firstname = "Ram"
    lastname = "Sam"
    email = "Sdonalgtig2@gmail.com"
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

        # UI Validation
        act_title = self.driver.title

        if act_title == "Your Account Has Been Created!":
            self.logger.info("Registration Successful")
            assert True
        else:
            self.logger.error("Registration Failed")
            self.driver.save_screenshot(
                "./Screenshots/RegisterFailed.png"
            )
            assert False


        # # Database Validations

        conn = DBConnection.get_connection()
        cursor = conn.cursor()

        query = """
                SELECT firstname, lastname, email, telephone
                FROM oc_customer
                WHERE email=%s
                """

        cursor.execute(query, (self.email,))
        result = cursor.fetchone()

        self.logger.info("Validating Customer Details in Database")

        assert result is not None, \
            f"Customer with email {self.email} not found in DB"

        assert result[0] == self.firstname
        assert result[1] == self.lastname
        assert result[2] == self.email
        assert result[3] == self.telephone

        self.logger.info("Database Validation Successful")

        cursor.close()
        conn.close()

        self.driver.close()

        self.logger.info("************* Register Test Completed *************")