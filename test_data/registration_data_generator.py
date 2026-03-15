from faker import Faker
from selenium.webdriver.support.expected_conditions import element_selection_state_to_be

from utilities.custom_types import Gender
import random

class RegistrationDataGenerator:
    def __init__(self):
        self.GENDER = random.choice([Gender.MALE, Gender.FEMALE])
        self.fake = Faker("pl_PL")
        if self.GENDER == Gender.FEMALE:
            self.FIRST_NAME = self.fake.first_name_female()
        else:
            self.FirstName = self.fake.first_name_male()


