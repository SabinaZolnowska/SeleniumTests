from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from header import adapters
import time

class Sandbox():

    def __init__(self):
        #super().__init__()
        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        options.add_argument('incognito')
        self.driver = webdriver.Chrome("chromedriver/chromedriver.exe", options=options)
        self.driver.maximize_window()
        self.nameDomain = "http://automationpractice.com/index.php"
        self.driver.get("http://automationpractice.com/index.php")
        self.timeout = 10
        #self.click_buttons()
        self.move_to()

    def click_buttons(self):
        adapters(self.driver).click_cart()
        adapters(self.driver).click_category_dresses()
        adapters(self.driver).click_category_tshirts()
        adapters(self.driver).click_category_women()
        adapters(self.driver).click_sign_in()
        adapters(self.driver).click_search_lup()
        adapters(self.driver).click_logo()
        adapters(self.driver).click_contact_us()

    def move_to(self):
        #header(self.driver).move_to_category_women()

        #header(self.driver).get_tops()
        #header(self.driver).move_to_tops()
        #header(self.driver).click_category_women_tops()
        #header(self.driver).click_category_women_tshirts()
        #header(self.driver).click_category_women_blouses()
        #header(self.driver).click_category_women_dresses()
        #header(self.driver).click_category_women_casual_dresses()
        #header(self.driver).click_category_women_evening_dresses()
        #header(self.driver).click_category_women_summer_dresses()
        #header(self.driver).click_category_dresses_casual_dresses()
        #header(self.driver).click_category_dresses_evening_dresses()
        #header(self.driver).click_category_dresses_summer_dresses()
        adapters(self.driver).search()
        time.sleep(10)
        self.driver.close()

x = Sandbox()
