import unittest
from footer.adapters import Footer
from selenium import webdriver

class TestFooter(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('incoginito')
        self.driver = webdriver.Chrome(options=options)
        self.timeout = 60
        self.footer = Footer(self.driver, self.timeout)
        self.driver.maximize_window()
        self.nameDomain = self.footer.URLs['home_page']
        self.driver.get(self.nameDomain)



    def test_get_newsletter_input(self):
        self.assertTrue(self.footer.get('newsletter_input'))

    def test_get_newsletter_submit(self):
        self.assertTrue(self.footer.get('newsletter_submit'))

    def test_get_facebook(self):
        self.assertTrue(self.footer.get('facebook'))

    def test_get_twitter(self):
        self.assertTrue(self.footer.get('twitter'))

    def test_get_youtube(self):
        self.assertTrue(self.footer.get('youtube'))

    def test_get_google_plus(self):
        self.assertTrue(self.footer.get('google_plus'))

    def test_get_women(self):
         self.assertTrue(self.footer.get('women'))

    def test_get_specials(self):
         self.assertTrue(self.footer.get('specials'))

    def test_get_new_products(self):
        self.assertTrue(self.footer.get('new_products'))

    def test_get_best_sellers(self):
        self.assertTrue(self.footer.get('best_sellers'))

    def test_get_our_stores(self):
        self.assertTrue(self.footer.get('our_stores'))

    def test_get_contact_us(self):
        self.assertTrue(self.footer.get('contact_us'))

    def test_get_terms_and_conditions_of_use(self):
        self.assertTrue(self.footer.get('terms_and_conditions_of_use'))

    def test_get_about_us(self):
        self.assertTrue(self.footer.get('about_us'))

    def test_get_sitemap(self):
        self.assertTrue(self.footer.get('sitemap'))

    def test_get_my_account(self):
        self.assertTrue(self.footer.get('my_account'))

    def test_get_my_orders(self):
        self.assertTrue(self.footer.get('my_orders'))

    def test_get_my_credit_slips(self):
        self.assertTrue(self.footer.get('my_credit_slips'))

    def test_get_my_addresses(self):
        self.assertTrue(self.footer.get('my_addresses'))

    def test_get_my_personal_info(self):
        self.assertTrue(self.footer.get('my_personal_info'))

    def test_get_emial(self):
        self.assertTrue(self.footer.get('email'))

    def test_get_phone_number(self):
        self.assertTrue(self.footer.get('phone_number'))

    def test_get_presta_shop(self):
        self.assertTrue(self.footer.get('presta_shop'))

    def test_click_presta_shop(self):
        self.footer.click('presta_shop')
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertEqual(self.driver.current_url, self.footer.URLs['presta_shop'])

    def test_click_my_personal_info(self):
        self.footer.click('my_personal_info')
        self.assertEqual(self.driver.current_url, self.footer.URLs['my_personal_info'])

    def test_click_my_addresses(self):
        self.footer.click('my_addresses')
        self.assertEqual(self.driver.current_url, self.footer.URLs['my_addresses'])

    def test_click_my_credit_slips(self):
        self.footer.click('my_credit_slips')
        self.assertEqual(self.driver.current_url, self.footer.URLs['my_credit_slips'])

    def test_click_my_orders(self):
        self.footer.click('my_orders')
        self.assertEqual(self.driver.current_url, self.footer.URLs['my_orders'])

    def test_click_my_account(self):
        self.footer.click('my_account')
        self.assertEqual(self.driver.current_url, self.footer.URLs['my_account'])

    def test_click_sitemap(self):
        self.footer.click('sitemap')
        self.assertEqual(self.driver.current_url, self.footer.URLs['sitemap'])

    def test_click_about_us(self):
        self.footer.click('about_us')
        self.assertEqual(self.driver.current_url, self.footer.URLs['about_us'])

    def test_click_terms_and_conditions_of_use(self):
        self.footer.click('terms_and_conditions_of_use')
        self.assertEqual(self.driver.current_url, self.footer.URLs['terms_and_conditions_of_use'])

    def test_click_contact_us(self):
        self.footer.click('contact_us')
        self.assertEqual(self.driver.current_url, self.footer.URLs['contact_us'])

    def test_click_our_stores(self):
        self.footer.click('our_stores')
        self.assertEqual(self.driver.current_url, self.footer.URLs['our_stores'])

    def test_click_best_sellers(self):
        self.footer.click('best_sellers')
        self.assertEqual(self.driver.current_url, self.footer.URLs['best_sellers']),

    def test_click_new_products(self):
        self.footer.click('new_products')
        self.assertEqual(self.driver.current_url, self.footer.URLs['new_products'])

    def test_click_specials(self):
        self.footer.click('specials')
        self.assertEqual(self.driver.current_url, self.footer.URLs['specials'])

    def test_click_women(self):
        self.footer.click('women')
        self.assertEqual(self.driver.current_url, self.footer.URLs['category_women'])

    def test_click_google_plus(self):
        self.footer.click('google_plus')
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertEqual(self.driver.current_url, self.footer.URLs['google_plus'])

    def test_click_youtube(self):
        self.footer.click('youtube')
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertEqual(self.driver.current_url, self.footer.URLs['youtube'])

    def test_click_twitter(self):
        self.footer.click('twitter')
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertEqual(self.driver.current_url, self.footer.URLs['twitter'])

    def test_click_facebook(self):
        self.footer.click('facebook')
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertEqual(self.driver.current_url, self.footer.URLs['facebook'])

    def test_click_newsletter_submit(self):
        self.footer.click('newsletter_submit')
        self.assertEqual(self.driver.current_url, self.footer.URLs['home_page'])

    def test_join_newsletter_already_registered(self, email='x@x.pl'):
        self.assertEqual(self.footer.join_newsletter(email),
                         self.footer.elements_text['newsletter_already_registered'])

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()