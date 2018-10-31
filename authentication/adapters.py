from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from authentication.locators import create_an_account_locators
from authentication.locators import login_in_locators
from mainActions.actions import MainActions

class Authentication_create_an_account(MainActions):

    def __init__(self, driver, timeout=60):
        self.driver = driver
        self.timeout = timeout
        super().__init__(self.driver, create_an_account_locators)