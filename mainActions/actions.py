from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class MainActions(object):

    def __init__(self, driver, locators, timeout=60):
        self.driver = driver
        self.timeout = timeout
        self.locators = locators

    def get(self, name):
        try:
            if self.locators[name]['type'] == 'xpath':
                return WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_element_located((By.XPATH, self.locators[name]['locator'])))
            elif self.locators[name]['type'] == 'id':
                return WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_element_located((By.ID, self.locators[name]['locator'])))
        except Exception as e:
            raise e

    def click(self, name):
        try:
            self.get(name).click()
            return self.driver.current_url
        except Exception as e:
            raise e

    def input(self, name, key):
        try:
            action = ActionChains(self.driver)
            action.click(self.get(name))
            action.send_keys(key)
            action.perform()
            return self.driver.current_url
        except Exception as e:
            raise e

    def get_element_text(self, name):
        try:
            return self.get(name).text
        except Exception as e:
            raise e

