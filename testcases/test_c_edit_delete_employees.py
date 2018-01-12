from utilize.base_test import BaseTest
import time


class UpdateEmployeesTestCases(BaseTest):
    def setUp(self):
        super().setUp()
        self.logger.info(" [*] Create new user with empty first name, should fail.")
        self.login(username=self.username, password=self.password)
        self.first_name = self.random_str()
        self.last_name = self.random_str()
        self.start_date = self.random_date()
        self.email = self.random_email()
        self.logger.info(" [*] Create new user : %s %s, should succeed." % (self.first_name, self.last_name))
        self.create_new_user(first_name=self.first_name,
                             last_name=self.last_name,
                             start_date=self.start_date,
                             email=self.email
                             )

    def test001_edit_user_with_valid_data(self):
        """ CAFEE-009

        * Edit user with valid data.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with valid data, should succeed.
        #. Edit user with valid data, should succeed.
        """
        old_username = "%s %s" % (self.first_name, self.last_name)
        self.first_name = self.random_str()
        self.last_name = self.random_str()
        self.start_date = self.random_date()
        self.email = self.random_email()
        self.logger.info(" [*] Edit user with valid data, should succeed.")
        self.edit_user(old_username=old_username,
                       first_name=self.first_name,
                       last_name=self.last_name,
                       start_date=self.start_date,
                       email=self.email
                       )
        new_username = "%s %s" % (self.first_name, self.last_name)
        self.assertTrue(self.is_user(new_username))

    def test002_edit_user_with_invalid_name(self):
        """ CAFEE-010

        * Edit user with invalid data.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with valid data, should succeed.
        #. Edit user with invalid name, should fail.
        """
        old_username = "%s %s" % (self.first_name, self.last_name)
        self.logger.info(" [*] Edit user with invalid name, should fail.")
        self.edit_user(old_username=old_username,
                       first_name='',
                       last_name='',
                       start_date=self.start_date,
                       email=self.email
                       )
        self.assertTrue(self.check_element_is_exist(element='back'), " [x] Update should fail!")
        self.click(element='back')
        time.sleep(2)
        self.assertTrue(self.is_user(old_username))

    def test003_edit_user_with_invalid_data(self):
        """ CAFEE-011

        * Edit user with invalid date.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with valid data, should succeed.
        #. Edit user with invalid date, should fail.
        """
        self.logger.info(" [*] Edit user with invalid data, should fail.")
        old_username = "%s %s" % (self.first_name, self.last_name)
        self.edit_user(old_username=old_username,
                       first_name=self.first_name,
                       last_name=self.last_name,
                       start_date="0000-00-00",
                       email=self.email
                       )
        time.sleep(2)
        self.assertTrue(self.check_element_is_exist(element='back'), " [x] Update should fail!")
        self.click(element='back')
        time.sleep(2)
        self.assertTrue(self.is_user(old_username))

    def test004_delete_user_from_main_page(self):
        """ CAFEE-012

        * Delete user from the main page.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with valid data, should succeed.
        #. Delete this new user, should succeed.
        """
        self.logger.info(" [*] Delete user from main page, should succeed.")
        self.delete_user(username="%s %s" % (self.first_name, self.last_name))
        time.sleep(3)
        self.assertFalse(self.is_user(username="%s %s" % (self.first_name, self.last_name)))

    def test005_delete_user_from_edit_page(self):
        """ CAFEE-013

        * Delete user from the edit page.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with valid data, should succeed.
        #. Go to the edit page.
        #. Delete user, should succeed.
        """
        self.logger.info(" [*] Delete user from edit page, should succeed.")
        self.delete_user_from_edit_page(username="%s %s" % (self.first_name, self.last_name))
        time.sleep(1)
        self.assertFalse(self.is_user(username="%s %s" % (self.first_name, self.last_name)))

    def tearDown(self):
        self.delete_user(username="%s %s" % (self.first_name, self.last_name))
        super().tearDown()
