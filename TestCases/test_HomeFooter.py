import pytest
from Pages.HomePageFooter import HomePageFooter
from Utilities.CustomLogger import LogGen
from Utilities.ReadProperties import ReadConfig
from Utilities.JsonReader import JsonReader


class Test_001_HomePage:

    base_url = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_verify_footer_links(self, setUp):

        self.driver = setUp
        self.driver.get(self.base_url)

        hp = HomePageFooter(self.driver)

        actual_information = hp.getInformationLinks()
        actual_customer_service = hp.getCustomerServiceLinks()
        actual_extras = hp.getExtrasLinks()
        actual_my_account = hp.getMyAccountLinks()

        expected_information = JsonReader.read_json(
            "./TestData/footerData.json",
            "information"
        )

        expected_customer_service = JsonReader.read_json(
            "./TestData/footerData.json",
            "customer_service"
        )

        expected_extras = JsonReader.read_json(
            "./TestData/footerData.json",
            "extras"
        )

        expected_my_account = JsonReader.read_json(
            "./TestData/footerData.json",
            "my_account"
        )

        if (
                actual_information == expected_information
                and actual_customer_service == expected_customer_service
                and actual_extras == expected_extras
                and actual_my_account == expected_my_account
        ):
            self.logger.info("************* Footer Links Verification Passed *************")
            assert True
        else:
            self.logger.error("************* Footer Links Verification Failed *************")
            assert False