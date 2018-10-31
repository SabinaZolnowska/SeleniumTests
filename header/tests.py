import unittest
from header.adapters import Header
from selenium import webdriver
from header.URLs import URLs


class TestHeader(unittest.TestCase):

    def setUp(self):
        self.URLs = URLs
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('incognito')
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.nameDomain = self.URLs['home_page']
        self.driver.get(self.nameDomain)
        self.timeout = 60
        self.header = Header(self.driver, self.timeout)

    def test_get_banner(self):
        self.assertTrue(self.header.get('banner'))

    def test_get_phone_number(self):
        self.assertTrue(self.header.get('phone_number'))

    def test_get_sign_in(self):
        self.assertTrue(self.header.get('sign_in'))

    def test_get_logo(self):
        self.assertTrue(self.header.get('logo'))

    def test_get_search_input(self):
        self.assertTrue(self.header.get('search_input'))

    def test_get_search_lup(self):
        self.assertTrue(self.header.get('search_lup'))

    def test_get_cart(self):
        self.assertTrue(self.header.get('cart'))

    def test_get_category_women(self):
        self.assertTrue(self.header.get('cat_women'))

    def test_get_category_dresses(self):
        self.assertTrue(self.header.get('cat_dresses'))

    def test_get_category_tshirts(self):
        self.assertTrue(self.header.get('cat_tshirts'))

    def test_get_contact_us(self):
        self.assertTrue(self.header.get('contact_us'))

    def test_get_category_women_tops(self):
        self.assertTrue(self.header.get('cat_women_tops'))

    def test_get_category_women_tshirts(self):
        self.assertTrue(self.header.get('cat_women_tshirts'))

    def test_get_category_women_blouses(self):
        self.assertTrue(self.header.get('cat_women_blouses'))

    def test_get_category_women_dresses(self):
        self.assertTrue(self.header.get('cat_women_dresses'))

    def test_get_category_women_casual_dresses(self):
        self.assertTrue(self.header.get('cat_women_casual_dresses'))

    def test_get_category_women_evening_dresses(self):
        self.assertTrue(self.header.get('cat_women_evening_dresses'))

    def test_get_category_women_summer_dresses(self):
        self.assertTrue(self.header.get('cat_women_summer_dresses'))

    def test_get_category_dresses_casual_dresses(self):
        self.assertTrue(self.header.get('cat_dresses_casual_dresses'))

    def test_get_category_dresses_evening_dresses(self):
        self.assertTrue(self.header.get('cat_dresses_evening_dresses'))

    def test_get_category_dresses_summer_dresses(self):
        self.assertTrue(self.header.get('cat_dresses_summer_dresses'))

    def test_search(self, key="dress"):
        self.header = Header(self.driver, self.timeout)
        self.header.input('search_input', key)

    def test_all(self):
        self.header = Header(self.driver, self.timeout)
        self.header.get('banner')
        self.header.get('phone_number')
        self.header.get('contact_us')
        self.header.click('contact_us')
        self.header.get('sign_in')
        self.header.click('sign_in')
        self.header.get('logo')
        self.header.click('logo')
        self.header.get('search_input')
        self.header.get('search_lup')
        self.header.click('search_lup')
        self.header.get('cart')
        self.header.click('cart')
        self.header.get('cat_women')
        self.header.click('cat_women')
        self.header.click_hover_subcategory('cat_women', 'cat_women_tops')
        self.header.click_hover_subcategory('cat_women', 'cat_women_tshirts')
        self.header.click_hover_subcategory('cat_women', 'cat_women_blouses')
        self.header.click_hover_subcategory('cat_women', 'cat_women_dresses')
        self.header.click_hover_subcategory('cat_women', 'cat_women_casual_dresses')
        self.header.click_hover_subcategory('cat_women', 'cat_women_evening_dresses')
        self.header.click_hover_subcategory('cat_women', 'cat_women_summer_dresses')
        self.header.get('cat_dresses')
        self.header.click('cat_dresses')
        self.header.click_hover_subcategory('cat_dresses', 'cat_dresses_casual_dresses')
        self.header.click_hover_subcategory('cat_dresses', 'cat_dresses_evening_dresses')
        self.header.click_hover_subcategory('cat_dresses', 'cat_dresses_summer_dresses')
        self.header.get('cat_tshirts')
        self.header.click('cat_tshirts')

        self.assertEqual(self.driver.current_url, self.URLs['category_tshirts'])

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

