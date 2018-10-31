from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from header.locators import header_locators
from mainActions.actions import MainActions


class Header(MainActions):

    def __init__(self, driver, timeout=60):
        self.driver = driver
        self.timeout = timeout
        super().__init__(self.driver, header_locators)

    def click_hover_subcategory(self, category, subcategory):
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.get(category))
            action.perform()
            action.click(self.get(subcategory))
            action.perform()
            return self.driver.current_url
        except Exception as e:
            raise e
