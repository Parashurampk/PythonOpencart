import pytest
from Pages.LoginPage import LoginPage
from Utilities.ReadProperties import ReadConfig
from Utilities.CustomLogger import LogGen
from Utilities import XLUtils
import time

class Test_002_DDT_Login:

    base_url = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setUp):

        self.logger.info("************* Test_002_DDT_Login started ****************")
        self.driver = setUp
        self.driver.get(self.base_url)

        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in Excel:", self.rows)

        lst_status = []

        for r in range(2, self.rows + 1):

            # Always go to login page before each iteration
            self.lp.clickMyAccountBtn()
            self.lp.clickLoginBtn()

            # Read data
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            # Login
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.doLogin()
            time.sleep(3)

            act_title = self.driver.title

            if act_title == "My Account":

                if self.exp == "pass":
                    lst_status.append("Pass")
                    self.lp.clickLogout()
                else:
                    lst_status.append("Fail")
                    self.lp.clickLogout()

            else:

                if self.exp == "fail":
                    lst_status.append("Pass")
                else:
                    lst_status.append("Fail")

        # Final Result
        if "Fail" not in lst_status:
            self.logger.info("DDT Login test passed")
            assert True
        else:
            self.logger.error("DDT Login test failed")
            assert False

        self.driver.close()
