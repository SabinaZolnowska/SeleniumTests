from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from HeaderLocators import HeaderLocators
from selenium.webdriver.common.keys import Keys
import time


class Header(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

        self.banner = HeaderLocators.banner
        self.phone_number = HeaderLocators.phone_number
        self.contact_us = HeaderLocators.contact_us
        self.sign_in = HeaderLocators.sign_in
        self.logo = HeaderLocators.logo
        self.search_input = HeaderLocators.search_input
        self.search_lup =  HeaderLocators.search_lup
        self.cart = HeaderLocators.cart

        self.category_women = HeaderLocators.category_women
        self.category_women_tops = HeaderLocators.category_women_tops
        self.category_women_tshirts = HeaderLocators.category_women_tshirts
        self.category_women_blouses = HeaderLocators.category_women_blouses
        self.category_women_dresses = HeaderLocators.category_women_dresses
        self.category_women_casual_dresses = HeaderLocators.category_women_casual_dresses
        self.category_women_evening_dresses = HeaderLocators.category_women_evening_dresses
        self.category_women_summer_dresses = HeaderLocators.category_women_summer_dresses

        self.category_dresses = HeaderLocators.category_dresses
        self.category_dresses_casual_dresses = HeaderLocators.category_dresses_casual_dresses
        self.category_dresses_evening_dresses = HeaderLocators.category_dresses_evening_dresses
        self.category_dresses_summer_dresses = HeaderLocators.category_dresses_summer_dresses

        self.category_tshirts = HeaderLocators.category_tshirts

    def get_banner(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, self.banner)))
        except Exception as e:
            raise e

    def get_phone_number(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, self.phone_number)))
        except Exception as e:
            raise e

    def get_contact_us(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, self.contact_us)))
        except Exception as e:
            raise e

    def click_contact_us(self):
        try:
            self.get_contact_us().click()
            return self.get_Current_URL()
        except Exception as e:
            raise e

    def get_sign_in(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, self.sign_in)))
        except Exception as e:
            raise e

    def click_sign_in(self):
        try:
            self.get_sign_in().click()
            return self.get_Current_URL()
        except Exception as e:
            raise e

    def get_logo(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, self.logo)))
        except Exception as e:
            raise e

    def click_logo(self):
        try:
            self.get_logo().click()
            return self.get_Current_URL()
        except Exception as e:
            raise e

    def get_search_input(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, self.search_input)))
        except Exception as e:
            raise e

    def search(self, key="dress"):
        try:
            action = ActionChains(self.driver)
            action.click(self.get_search_input())
            action.send_keys(key)
            action.click(self.get_search_lup())
            action.perform()
            return self.get_Current_URL()
        except Exception as e:
            raise e

    def get_search_lup(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, self.search_lup)))
        except Exception as e:
            raise e

    def click_search_lup(self):
        try:
            self.get_search_lup().click()
            return self.get_Current_URL()
        except Exception as e:
            raise e

    def get_cart(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, self.cart)))
        except Exception as e:
            raise e

    def click_cart(self):
        try:
            self.get_cart().click()
            return self.get_Current_URL()
        except Exception as e:
            raise e

    def get_category_women(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, self.category_women)))
        except Exception as e:
            raise e

    def click_category_women(self):
        try:
            self.get_category_women().click()
            return self.get_Current_URL()
        except Exception as e:
            raise e

    def click_category_women_tops(self):
        def get_category_women_tops():
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, self.category_women_tops)))
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.get_category_women())
            action.perform()
            action.click(get_category_women_tops())
            action.perform()
            return self.get_Current_URL()
        except Exception as e:
            raise e

    def click_category_women_tshirts(self):
        def get_category_women_tshirts():
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, self.category_women_tshirts)))
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.get_category_women())
            action.perform()
            action.click(get_category_women_tshirts())
            action.perform()
            return self.get_Current_URL()
        except Exception as e:
            raise e

    def click_category_women_blouses(self):
        def get_category_women_blouses():
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, self.category_women_blouses)))
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.get_category_women())
            action.perform()
            action.click(get_category_women_blouses())
            action.perform()
            return self.get_Current_URL()
        except Exception as e:
            raise e


    def click_category_women_dresses(self):
        def get_category_women_dresses():
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, self.category_women_dresses)))
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.get_category_women())
            action.perform()
            action.click(get_category_women_dresses())
            action.perform()
            return self.get_Current_URL()
        except Exception as e:
            raise e

    def click_category_women_casual_dresses(self):
        def get_category_women_casual_dresses():
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, self.category_women_casual_dresses)))
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.get_category_women())
            action.perform()
            action.click(get_category_women_casual_dresses())
            action.perform()
            return self.get_Current_URL()
        except Exception as e:
            raise e

    def click_category_women_evening_dresses(self):
        def get_category_women_evening_dresses():
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, self.category_women_evening_dresses)))
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.get_category_women())
            action.perform()
            action.click(get_category_women_evening_dresses())
            action.perform()
            return self.get_Current_URL()
        except Exception as e:
            raise e

    def click_category_women_summer_dresses(self):
        def get_category_women_summer_dresses():
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, self.category_women_summer_dresses)))
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.get_category_women())
            action.perform()
            action.click(get_category_women_summer_dresses())
            action.perform()
            return self.get_Current_URL()
        except Exception as e:
            raise  e

    def get_category_dresses(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, self.category_dresses)))
        except Exception as e:
            raise e

    def click_category_dresses(self):
        try:
            self.get_category_dresses().click()
            return self.get_Current_URL()
        except Exception as e:
            raise e

    def click_category_dresses_casual_dresses(self):
        def get_category_dresses_casual_dresses():
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, self.category_dresses_casual_dresses)))
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.get_category_dresses())
            action.perform()
            action.click(get_category_dresses_casual_dresses())
            action.perform()
            return self.get_Current_URL()
        except Exception as e:
            raise e

    def click_category_dresses_evening_dresses(self):
        def get_category_dresses_evening_dresses():
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, self.category_dresses_evening_dresses)))
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.get_category_dresses())
            action.perform()
            action.click(get_category_dresses_evening_dresses())
            action.perform()
            return self.get_Current_URL()
        except Exception as e:
            raise e

    def click_category_dresses_summer_dresses(self):
        def get_category_dresses_summer_dresses():
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, self.category_dresses_summer_dresses)))
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.get_category_dresses())
            action.perform()
            action.click(get_category_dresses_summer_dresses())
            action.perform()
            return self.get_Current_URL()
        except Exception as e:
            raise e

    def get_category_tshirts(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, self.category_tshirts)))
        except Exception as e:
            raise e

    def click_category_tshirts(self):
        try:
            self.get_category_tshirts().click()
            return self.get_Current_URL()
        except Exception as e:
            raise e

    def close(self):
        try:
            self.driver.close()
        except Exception as e:
            raise e

    def get_Current_URL(self):
        try:
            return self.driver.current_url
        except Exception as e:
            raise e
