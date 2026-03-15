from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage
from utilities.custom_types import Gender


class Locators:
    FIRST_NAME = (By.ID, "customer_firstname")
    GENDER_MALE = (By.XPATH, '//label[@for="id_gender1"]')
    GENDER_FEMALE = (By.XPATH, '//label[@for="id_gender2"]')
    EMAIL_EMAIL_ENTERED = (By.ID, 'email')


class CreateAccountPage(BasePage):
    def choose_gender(self, gender):
        """
        Choose Mr or Mrs
        """
        if gender == Gender.MALE:
            self.driver.find_element(*Locators.GENDER_MALE).click()
        else:
            self.driver.find_element(*Locators.GENDER_FEMALE).click()

    def enter_first_name(self, first_name):
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(first_name)

    def get_entered_email(self):

       return self.driver.find_element(*Locators.EMAIL_EMAIL_ENTERED).get_attribute('value')

    def _verify_page(self):
      #TODO: Improve this!(brzydki zapis)
        sleep(3)

