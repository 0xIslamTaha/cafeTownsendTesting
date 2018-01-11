from utilize.base_test import BaseTest
import time
from parameterized import parameterized


class CreateEmployeesTestCases(BaseTest):
    def setUp(self):
        super().setUp()
        self.login(username=self.username, password=self.password)

    def test001_create_new_user_with_valid_data(self):
        """ CAFEE-004

        * Crete new user with valid data.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with valid data, should succeed.
        """
        first_name = self.random_str()
        last_name = self.random_str()
        start_date = self.random_date()
        email = self.random_email()
        self.create_new_user(first_name=first_name,
                             last_name=last_name,
                             start_date=start_date,
                             email=email
                             )
        self.assertTrue(self.is_user(username="%s %s" % (first_name, last_name)))
        self.delete_user(username="%s %s" % (first_name, last_name))

    def test002_create_new_user_with_invalid_firstname(self):
        """ CAFEE-005

        * Crete new user with empty first name.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with empty first name, should fail.
        """
        self.create_new_user(first_name='',
                             last_name=self.random_str(),
                             start_date=self.random_date(),
                             email=self.random_email()
                             )
        time.sleep(1)
        self.assertIn('new', self.get_url())

    def test003_create_new_user_with_invalid_lastname(self):
        """ CAFEE-006

        * Crete new user with empty last name.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with empty last name, should fail.
        """
        self.create_new_user(first_name=self.random_str(),
                             last_name='',
                             start_date=self.random_date(),
                             email=self.random_email()
                             )
        time.sleep(1)
        self.assertIn('new', self.get_url())

    @parameterized.expand([('empty', ''),
                           ('invalid_day_1', '2017-10-00'),
                           ('invalid_day_2', '2017-1-09'),
                           ('invalid_day_3', '2017-20-01'),
                           ('invalid_day_4', '2017-02-31')
                           ])
    def test005_create_new_user_with_invalid_date(self, reason, date):
        """ CAFEE-007

        * Crete new user with invalid email.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with invalid date, should fail.
        """
        self.create_new_user(first_name=self.random_str(),
                             last_name=self.random_str(),
                             start_date=date,
                             email=self.random_email()
                             )
        time.sleep(1)
        try:
            alert = self.driver.switch_to_alert()
            self.assertIn("Error", alert.text)
            alert.accept()
        except:
            self.assertIn('new', self.get_url())

    def test005_create_new_user_with_invalid_email(self):
        """ CAFEE-008

        * Crete new user with empty last name.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with empty email, should fail.
        """
        self.create_new_user(first_name=self.random_str(),
                             last_name='',
                             start_date=self.random_date(),
                             email=self.random_email()
                             )
        time.sleep(1)
        self.assertIn('new', self.get_url())

