from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from footer.locators import footer_locators
from mainActions.actions import MainActions
from footer.URL import URLs
from footer.elements_text import element_text

class Footer(MainActions):

    def __init__(self, driver, timeout=60):
        self.driver = driver
        self.timeout = timeout
        self.URLs = URLs
        self.elements_text = element_text
        super().__init__(self.driver, footer_locators)

    def join_newsletter(self, email):
        try:
            action = ActionChains(self.driver)
            action.click(self.get('newsletter_input'))
            action.send_keys(email)
            action.click(self.get('newsletter_submit'))
            action.perform()
            return self.get_element_text('newsletter_message')
        except Exception as e:
            raise e