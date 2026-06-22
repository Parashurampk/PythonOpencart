import pytest
from Pages.HomePage import HomePage
from Utilities.CustomLogger import LogGen
from Utilities.ReadProperties import ReadConfig
from Utilities.JsonReader import JsonReader


class Test_001_HomePage:

    base_url = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_verify_featured_products(self, setUp):
        self.driver = setUp
        self.driver.get(self.base_url)
        hp = HomePage(self.driver)

        actual_products = hp.getFeaturedProducts()
        expected_products = JsonReader.read_json(
            "./TestData/HomePageData.json",
            "featured_products"
        )

        self.logger.info(f"Actual Products : {actual_products}")
        self.logger.info(f"Expected Products : {expected_products}")

        if all(product in actual_products for product in expected_products):
            self.logger.info("************* Featured Products Verification Passed *************")
            assert True
        else:
            self.logger.error("************* Featured Products Verification Failed *************")
            assert False

    @pytest.mark.sanity
    def test_verify_menu_tabs(self, setUp):

        self.driver = setUp
        self.driver.get(self.base_url)

        hp = HomePage(self.driver)

        actual_menus = hp.getMenuTabs()
        expected_menus = JsonReader.read_json(
            "./TestData/HomePageData.json",
            "menu_tabs"
        )

        self.logger.info(f"Actual Menus : {actual_menus}")
        self.logger.info(f"Expected Menus : {expected_menus}")

        if actual_menus == expected_menus:
            self.logger.info("************* Menu Tabs Verification Passed *************")
            assert True
        else:
            self.logger.error("************* Menu Tabs Verification Failed *************")
            assert False