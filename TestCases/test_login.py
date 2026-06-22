import pytest
from Pages.LoginPage import LoginPage
from Utilities.ReadProperties import ReadConfig
from Utilities.CustomLogger import LogGen

class Test_001_Login:

    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self, setUp):

        self.logger.info("************* Verifying Home Page Title *************")
        self.driver = setUp
        self.driver.get(self.base_url)

        act_title = self.driver.title
        act_title = self.driver.title

        if act_title == "Your Store":
            self.logger.info("************* Home page Title is passed *************")
            assert True
        else:
            self.logger.error("************* Home page Title is failed *************" )
            assert False

    @pytest.mark.smoke
    def test_loginPage(self, setUp):

        self.logger.info("************* Verifying Login *************")
        self.driver = setUp
        self.driver.get(self.base_url)

        lp = LoginPage(self.driver)

        lp.clickMyAccountBtn()
        lp.clickLoginBtn()

        lp.setUsername(self.username)
        lp.setPassword(self.password)

        lp.doLogin()

        act_title = self.driver.title
        self.logger.info(f"Actual Title after Login: {act_title}")

        if act_title == "My Account":
            self.logger.info("************* Login Test is Passed *************")
            assert True
        else:
            self.logger.error("************* Login Test is Failed *************")
            assert False