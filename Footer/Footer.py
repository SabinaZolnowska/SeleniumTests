from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from FooterLocators import FooterLocators as FL


class Footer(object):

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout


    def get_newsletter_input(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['newsletter_input'])))
        except Exception as e:
            raise e

    def get_newsletter_submit(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['newsletter_submit'])))
        except Exception as e:
            raise e

    def click_newsletter_submit(self):
        try:
            self.get_newsletter_submit().click()
            return self.get_current_URL()
        except Exception as e:
            raise e

    def join_newsletter(self, email = 'x@x.pl'):
        def get_join_newsletter_message():
            try:
                return WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_element_located((By.XPATH, FL['newsletter_message']))).text
            except Exception as e:
                raise e
        try:
            action = ActionChains(self.driver)
            action.click(self.get_newsletter_input())
            action.send_keys(email)
            action.click(self.get_newsletter_submit())
            action.perform()
            return get_join_newsletter_message()
        except Exception as e:
            raise e

    def get_facebook(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['facebook'])))
        except Exception as e:
            raise e

    def click_facebook(self):
        def get_facebook_fanpage_message():
            try:
                return WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_element_located((By.XPATH, FL['facebook_fanpage_message'])))
            except Exception as e:
                raise e
        try:
            self.get_facebook().click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            return get_facebook_fanpage_message().text
        except Exception as e:
            raise e

    def get_twitter(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['twitter'])))
        except Exception as e:
            raise e

    def click_twitter(self):
        def get_twitter_profile_message():
            try:
                return WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_element_located((By.XPATH, FL['twitter_profile_message'])))
            except Exception as e:
                raise e
        try:
            self.get_twitter().click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            return get_twitter_profile_message().text
        except Exception as e:
            raise e

    def get_youtube(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['youtube'])))
        except Exception as e:
            raise e

    def click_youtube(self):
        def get_youtube_channel_name():
            try:
                return WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_element_located((By.XPATH, FL['youtube_channel_name'])))
            except Exception as e:
                raise e
        try:
            self.get_youtube().click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            return get_youtube_channel_name().text
        except Exception as e:
            raise e

    def get_google_plus(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['google_plus'])))
        except Exception as e:
            raise e

    def click_google_plus(self):
        def get_google_plus_profile_name():
            try:
                return WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_element_located((By.XPATH, FL['google_plus_profile_name'])))
            except Exception as e:
                raise e
        try:
            self.get_google_plus().click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            return get_google_plus_profile_name().text
        except Exception as e:
            raise e

    def get_women(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['women'])))
        except Exception as e:
            raise e

    def click_women(self):
        try:
            self.get_women().click()
            return self.get_current_URL()
        except Exception as e:
            raise e

    def get_specials(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['specials'])))
        except Exception as e:
            raise e

    def click_specials(self):
        try:
            self.get_specials().click()
            return self.get_current_URL()
        except Exception as e:
            raise e

    def get_new_products(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['new_products'])))
        except Exception as e:
            raise e

    def click_new_products(self):
        try:
            self.get_new_products().click()
            return self.get_current_URL()
        except Exception as e:
            raise e

    def get_best_sellers(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['best_sellers'])))
        except Exception as e:
            raise e

    def click_best_sellers(self):
        try:
            self.get_best_sellers().click()
            return self.get_current_URL()
        except Exception as e:
            raise e

    def get_our_stores(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['our_stores'])))
        except Exception as e:
            raise e

    def click_our_stores(self):
        try:
            self.get_our_stores().click()
            return self.get_current_URL()
        except Exception as e:
            raise e

    def get_contact_us(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['contact_us'])))
        except Exception as e:
            raise e

    def click_contact_us(self):
        try:
            self.get_contact_us().click()
            return self.get_current_URL()
        except Exception as e:
            raise e

    def get_terms_and_conditions_of_use(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['terms_and_conditions_of_use'])))
        except Exception as e:
            raise e

    def click_terms_and_conditions_of_use(self):
        try:
            self.get_terms_and_conditions_of_use().click()
            return self.get_current_URL()
        except Exception as e:
            raise e

    def get_about_us(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['about_us'])))
        except Exception as e:
            raise e

    def click_about_us(self):
        try:
            self.get_about_us().click()
            return self.get_current_URL()
        except Exception as e:
            raise e

    def get_sitemap(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['sitemap'])))
        except Exception as e:
            raise e

    def click_sitemap(self):
        try:
            self.get_sitemap().click()
            return self.get_current_URL()
        except Exception as e:
            raise e

    def get_my_account(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['my_account'])))
        except Exception as e:
            raise e

    def click_my_account(self):
        try:
            self.get_my_account().click()
            return self.get_current_URL()
        except Exception as e:
            raise e

    def get_my_orders(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['my_orders'])))
        except Exception as e:
            raise e

    def click_my_orders(self):
        try:
            self.get_my_orders().click()
            return self.get_current_URL()
        except Exception as e:
            raise e

    def get_my_credit_slips(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['my_credit_slips'])))
        except Exception as e:
            raise e

    def click_my_credit_slips(self):
        try:
            self.get_my_credit_slips().click()
            return self.get_current_URL()
        except Exception as e:
            raise e

    def get_my_addresses(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['my_addresses'])))
        except Exception as e:
            raise e

    def click_my_addresses(self):
        try:
            self.get_my_addresses().click()
            return self.get_current_URL()
        except Exception as e:
            raise e

    def get_my_personal_info(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['my_personal_info'])))
        except Exception as e:
            raise e

    def click_my_personal_info(self):
        try:
            self.get_my_personal_info().click()
            return self.get_current_URL()
        except Exception as e:
            raise e

    def get_email(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['email'])))
        except Exception as e:
            raise e

    def get_phone_number(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['phone_number'])))
        except Exception as e:
            raise e

    def get_presta_shop(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, FL['presta_shop'])))
        except Exception as e:
            raise e

    def click_presta_shop(self):
        try:
            self.get_presta_shop().click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            return self.get_current_URL()
        except Exception as e:
            raise e

    def close(self):
        try:
            self.driver.close()
        except Exception as e:
            raise e

    def get_current_URL(self):
        try:
            return self.driver.current_url
        except Exception as e:
            raise e
"""
for keys, values in FL.items():
    print (keys, values)


x = Footer()

x.join_newsletter()
x.get_specials()
x.get_phone_number()
x.get_presta_shop()
x.get_my_personal_info()
x.get_my_addresses()
x.get_my_credit_slips()
x.get_sitemap()
x.get_terms_and_conditions_of_use()
x.get_contact_us()
x.get_our_stores()
x.get_best_sellers()
x.get_new_products()
x.get_youtube()
x.get_twitter()
x.get_facebook()
x.get_newsletter_submit()
x.get_newsletter_input()
x.get_women()
x.get_about_us()
x.get_email()
x.get_google_plus()

print(x.click_women())
sleep(10)
"""