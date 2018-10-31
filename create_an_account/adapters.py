from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from create_an_account.locators import create_an_account_locators
from mainActions.actions import MainActions

class Create_an_account(MainActions):


    def __init__(self, driver, timeout=60):
        self.driver = driver
        self.timeout = timeout
        super().__init__(self.driver, create_an_account_locators)

    def select_brith_day(self, number_of_day=10):
        if 0 < number_of_day < 32:
            select = Select(self.get("dropdown_brith_day"))
            select.select_by_index(number_of_day)

    def select_brith_month(self, number_of_month=8):
        if 0 < number_of_month < 13:
            select = Select(self.get("dropdown_brith_month"))
            select.select_by_index(number_of_month)

    def select_brith_year(self, number_of_year=25):
        if 0 < number_of_year < 119:
            select = Select(self.get("dropdown_brith_year"))
            select.select_by_index(number_of_year)

    def select_state(self, number_of_state=40):
        if 0 < number_of_state < 52:
            select = Select(self.get("dropdown_state"))
            select.select_by_index(number_of_state)