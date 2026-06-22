import pytest

from Pages.AddressMenuPage import AddressMenuPage
from Utilities.CustomLogger import LogGen


class Test_001_AddressPage:

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_verify_address_menu(self, login):

        self.logger.info("***** Test Address Menu Started *****")

        # login fixture already performed login
        self.driver = login

        address_page = AddressMenuPage(self.driver)

        # Get menu count
        menu_count = address_page.get_address_menu_count()
        self.logger.info(f"Menu Count: {menu_count}")
        print("Menu Count is :--", menu_count)

        expected_menu = [

            "My Account",
            "Edit Account",
            "Password",
            "Address Book",
            "Wish List",
            "Order History",
            "Downloads",
            "Recurring payments",
            "Reward Points",
            "Returns",
            "Transactions",
            "Newsletter",
            "Logout"

        ]
        # Verify count
        assert menu_count == len(expected_menu)

        # Get menu texts
        menu_texts = address_page.get_address_menu_texts()
        self.logger.info(f"Menu Texts: {menu_texts}")
        print(menu_texts)

        # Verify menu names
        assert menu_texts == expected_menu
        self.logger.info("***** Test Address Menu Completed *****")