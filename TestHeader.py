import unittest
from Header import Header
from URLs import URLs
from selenium import webdriver


class TestHeader(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('incognito')
        self.driver = webdriver.Chrome("chromedriver/chromedriver.exe", options=options)
        self.driver.maximize_window()
        self.nameDomain = "http://automationpractice.com/index.php"
        self.driver.get(self.nameDomain)
        self.timeout = 10

    def test_get_banner(self):
        self.assertTrue(Header(self.driver).get_banner())

    def test_get_phone_number(self):
        self.assertTrue(Header(self.driver).get_phone_number())

    def test_get_contact_us(self):
        self.assertTrue(Header(self.driver).get_contact_us())

    def test_get_sign_in(self):
        self.assertTrue(Header(self.driver).get_sign_in())

    def test_get_logo(self):
        self.assertTrue(Header(self.driver).get_logo())

    def test_get_search_input(self):
        self.assertTrue(Header(self.driver).get_search_input())

    def test_get_search_lup(self):
        self.assertTrue(Header(self.driver).get_search_lup())

    def test_get_cart(self):
        self.assertTrue(Header(self.driver).get_cart())

    def test_get_category_women(self):
        self.assertTrue(Header(self.driver).get_category_women())

    def test_get_category_dresses(self):
        self.assertTrue(Header(self.driver).get_category_dresses())

    def test_get_category_tshirts(self):
        self.assertTrue(Header(self.driver).get_category_tshirts())


    def test_click_contact_us(self):
        self.assertEqual(Header(self.driver).click_contact_us(), URLs.contact_us)

    def test_click_sign_in(self):
        self.assertEqual(Header(self.driver).click_sign_in(), URLs.sign_in)

    def test_click_logo(self):
        self.assertEqual(Header(self.driver).click_logo(),URLs.home_page)

    def test_click_search_lup(self):
        self.assertEqual(Header(self.driver).click_search_lup(), URLs.search_empty)

    def test_click_cart(self):
        self.assertEqual(Header(self.driver).click_cart(), URLs.cart_empty)

    def test_click_category_women(self):
        self.assertEqual(Header(self.driver).click_category_women(), URLs.category_women)

    def test_click_category_women_tops(self):
        self.assertEqual(Header(self.driver).click_category_women_tops(), URLs.category_tops)

    def test_click_category_women_tshirts(self):
        self.assertEqual(Header(self.driver).click_category_women_tshirts(), URLs.category_tshirts)

    def test_click_category_women_blouses(self):
        self.assertEqual(Header(self.driver).click_category_women_blouses(), URLs.category_blouses)

    def test_click_category_women_dresses(self):
        self.assertEqual(Header(self.driver).click_category_women_dresses(), URLs.category_dresses)

    def test_click_category_women_casual_dresses(self):
        self.assertEqual(Header(self.driver).click_category_women_casual_dresses(), URLs.category_casual_dresses)

    def test_click_category_women_evening_dresses(self):
        self.assertEqual(Header(self.driver).click_category_women_evening_dresses(), URLs.category_evening_dresses)

    def test_click_category_women_summer_dresses(self):
        self.assertEqual(Header(self.driver).click_category_women_summer_dresses(), URLs.category_summer_dresses)

    def test_click_category_dresses(self):
        self.assertEqual(Header(self.driver).click_category_dresses(), URLs.category_dresses)

    def test_click_category_dresses_casual_dresses(self):
        self.assertEqual(Header(self.driver).click_category_dresses_casual_dresses(), URLs.category_casual_dresses)

    def test_click_category_dresses_evening_dresses(self):
        self.assertEqual(Header(self.driver).click_category_dresses_evening_dresses(), URLs.category_evening_dresses)

    def test_click_category_dresses_summer_dresses(self):
        self.assertEqual(Header(self.driver).click_category_dresses_summer_dresses(), URLs.category_summer_dresses)

    def test_click_category_tshirts(self):
        self.assertEqual(Header(self.driver).click_category_tshirts(), URLs.category_tshirts)

    def test_search(self):
        self.assertEqual(Header(self.driver).search(), URLs.search_dress)

    def test_all(self):
        header = Header(self.driver)
        header.get_banner()
        header.get_phone_number()
        header.get_contact_us()
        header.click_contact_us()
        header.get_sign_in()
        header.click_sign_in()
        header.get_logo()
        header.click_logo()
        header.get_search_input()
        header.get_search_lup()
        header.click_search_lup()
        header.get_cart()
        header.click_cart()
        header.get_category_women()
        header.click_category_women()
        header.click_category_women_tops()
        header.click_category_women_tshirts()
        header.click_category_women_blouses()
        header.click_category_women_dresses()
        header.click_category_women_casual_dresses()
        header.click_category_women_evening_dresses()
        header.click_category_women_summer_dresses()
        header.get_category_dresses()
        header.click_category_dresses()
        header.click_category_dresses_casual_dresses()
        header.click_category_dresses_evening_dresses()
        header.click_category_dresses_summer_dresses()
        header.get_category_tshirts()
        header.click_category_tshirts()

        self.assertEqual(header.get_Current_URL(), URLs.category_tshirts)

    def tearDown(self):
        Header(self.driver).close()

if __name__ == '__main__':
    unittest.main()