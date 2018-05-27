import unittest
from Footer import Footer
from URLs2 import URLs
from URLs2 import Messages
from selenium import webdriver


class TestFooter(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('incoginito')
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(URLs['home_page'])
        self.timeout = 10


    def test_get_newsletter_input(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_newsletter_input())

    def test_get_newsletter_submit(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_newsletter_submit())

    def test_get_facebook(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_facebook())

    def test_get_twitter(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_twitter())

    def test_get_youtube(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_youtube())

    def test_get_google_plus(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_google_plus())

    def test_get_women(self):
         self.assertTrue(Footer(self.driver, self.timeout).get_women())

    def test_get_specials(self):
         self.assertTrue(Footer(self.driver, self.timeout).get_specials())

    def test_get_new_products(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_new_products())

    def test_get_best_sellers(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_best_sellers())

    def test_get_our_stores(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_our_stores())

    def test_get_contact_us(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_contact_us())

    def test_get_terms_and_conditions_of_use(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_terms_and_conditions_of_use())

    def test_get_about_us(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_about_us())

    def test_get_sitemap(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_sitemap())

    def test_get_my_account(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_my_account())

    def test_get_my_orders(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_my_orders())

    def test_get_my_credit_slips(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_my_credit_slips())

    def test_get_my_addresses(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_my_addresses())

    def test_get_my_personal_info(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_my_personal_info())

    def test_get_emial(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_email())

    def test_get_phone_number(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_phone_number())

    def test_get_presta_shop(self):
        self.assertTrue(Footer(self.driver, self.timeout).get_presta_shop())

    def test_click_presta_shop(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_presta_shop(), URLs['presta_shop'])

    def test_click_my_personal_info(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_my_personal_info(), URLs['my_personal_info'])

    def test_click_my_addresses(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_my_addresses(), URLs['my_addresses'])

    def test_click_my_credit_slips(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_my_credit_slips(), URLs['my_credit_slips'])

    def test_click_my_orders(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_my_orders(), URLs['my_orders'])

    def test_click_my_account(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_my_account(), URLs['my_account'])

    def test_click_sitemap(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_sitemap(), URLs['sitemap'])

    def test_click_about_us(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_about_us(), URLs['about_us'])

    def test_click_terms_and_conditions_of_use(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_terms_and_conditions_of_use(),
                         URLs['terms_and_conditions_of_use'])

    def test_click_contact_us(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_contact_us(), URLs['contact_us'])

    def test_click_our_stores(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_our_stores(), URLs['our_stores'])

    def test_click_best_sellers(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_best_sellers(), URLs['best_sellers']),

    def test_click_new_products(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_new_products(), URLs['new_products'])

    def test_click_specials(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_specials(), URLs['specials'])

    def test_click_women(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_women(), URLs['category_women'])

    def test_click_google_plus(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_google_plus(), Messages['google_plus_profile_name'])

    def test_click_youtube(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_youtube(), Messages['youtube_channel_name'])

    def test_click_twitter(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_twitter(), Messages['twitter_profile'])

    def test_click_facebook(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_facebook(), Messages['facebook_fanpage'])

    def test_click_newsletter_submit(self):
        self.assertEqual(Footer(self.driver, self.timeout).click_newsletter_submit(), URLs['home_page'])

    def test_join_newsletter(self, email='x@x.pl'):
        self.assertEqual(Footer(self.driver, self.timeout).join_newsletter(
            email), Messages['newsletter_incorrect_join'])

    def test_get_current_URL(self):
        self.assertEqual(Footer(self.driver, self.timeout).get_current_URL(), URLs['home_page'])

    def tearDown(self):
        Footer(self.driver).close()


if __name__ == '__main__':
    unittest.main()