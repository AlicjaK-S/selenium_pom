from test_data.registration_data_generator import RegistrationDataGenerator
from tests.base_tests import BaseTest
from time import sleep

class RegistrationTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.data = RegistrationDataGenerator()
        self.authentication_page = self.home_page.click_sign_in()
        self.authentication_page.enter_create_account_email(self.data.EMAIL)
        self.create_account_page = self.authentication_page.click_create_account()

    def testNoLastname(self):
        self.create_account_page.enter_first_name(self.data.FIRST_NAME)
        self.create_account_page.choose_gender(self.data.GENDER)
        print(self.create_account_page.get_entered_email())
        print(self.data.EMAIL)
        self.assertEqual(self.data.EMAIL, self.create_account_page.get_entered_email())

        sleep(3)

