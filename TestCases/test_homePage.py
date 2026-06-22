import pytest
from Pages.HomePage import HomePage
from Utilities.CustomLogger import LogGen
from Utilities.ReadProperties import ReadConfig


class Test_001_HomePage:

    base_url = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_verify_featured_products(self, setUp):

        self.logger.info("************* Verifying Featured Products *************")

        self.driver = setUp
        self.driver.get(self.base_url)
        hp = HomePage(self.driver)
        actual_products = hp.getFeaturedProducts()

        self.logger.info(f"Actual Products Found: {actual_products}")

        expected_products = [
            "MacBook",
            "iPhone",
            'Apple Cinema 30"',
            "Canon EOS 5D"
        ]

        if all(product in actual_products for product in expected_products):
            self.logger.info("************* Featured Products Verification Passed *************")
            assert True
        else:
            self.logger.error("************* Featured Products Verification Failed *************")
            assert False

