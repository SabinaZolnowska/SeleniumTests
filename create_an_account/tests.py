import unittest
from create_an_account.adapters import Create_an_account
from selenium import webdriver
from header.adapters import Header
from authentication.adapters import Authentication_create_an_account


class Test_Create_an_account(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        options.add_argument('incoginito')
        self.driver = webdriver.Chrome(options=options)
        self.timeout = 60
        self.create_an_account = Create_an_account(self.driver, self.timeout)
        self.driver.maximize_window()
        self.nameDomain = "http://automationpractice.com"
        self.driver.get(self.nameDomain)


    def test_create_account(self):
        Header(self.driver, self.timeout).click('sign_in')
        Authentication_create_an_account(self.driver, self.timeout).input("input_email", "wefwefewf@edfdfdf.ff")
        Authentication_create_an_account(self.driver, self.timeout).click("btn_submit_create_an_account")
        self.create_an_account.click("radiobox_mrs")
        self.create_an_account.input("input_first_name", "aaaa")
        self.create_an_account.input("input_last_name", "bbbb")
        self.create_an_account.input("input_password", "test1234")
        self.create_an_account.select_brith_day(15)
        self.create_an_account.select_brith_month()
        self.create_an_account.select_brith_year()
        self.create_an_account.input("input_address_first_name", "zzzz")
        self.create_an_account.input("input_address_last_name", "www")
        self.create_an_account.input("input_company", "firma")
        self.create_an_account.input("input_address_1", "address1")
        self.create_an_account.input("input_address_2", "address2")
        self.create_an_account.input("input_city", "miasto")
        self.create_an_account.select_state()
        self.create_an_account.input("input_zip_code", "12345")
        self.create_an_account.input('input_additional_information', 'input_alias_address')
        self.create_an_account.input('input_home_phone', "123456789")
        self.create_an_account.input('input_mobile_phone', "987654321")
        self.create_an_account.get("input_alias_address").clear()
        self.create_an_account.input("input_alias_address", "aaaa")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()