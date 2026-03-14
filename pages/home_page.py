from selenium.webdriver.common.by import By
from pages.authentication_page import AuthenticationPage
from pages.base_page import BasePage

class Locators:
    SIGN_IN_LINK = (By.CLASS_NAME, "login")
class HomePage(BasePage):
    def click_sign_in(self):
        self.driver.find_element(*Locators.SIGN_IN_LINK).click()
        return AuthenticationPage(self.driver)
