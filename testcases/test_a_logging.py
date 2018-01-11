from utilize.base_test import BaseTest


class LoggingTestCases(BaseTest):
    def test001_login_active(self):
        """ CAFEE-001

        * Test login with provider credential.
        **Test Scenario:**
        #. Get login page
        #. Enter the correct username and password
        #. Press on "Login" button
        #. Check that login is done, Should succeed.
        """
        self.login(username=self.username, password=self.password)
        self.assertIn(self.username, self.get_text(element="greetings"))

    def test002_login_passive(self):
        """ CAFEE-002

        * Test login with random credential.
        **Test Scenario:**
        #. Get login page
        #. Enter the random username and password
        #. Press on "Login" button
        #. Check that login is failed, Should succeed.
        """
        self.login(username=self.random_str(), password=self.random_str())
        self.assertIn("Invalid username or password!", self.get_text(element="invalid_login"))

    def test003_logout(self):
        """ CAFEE-003

        * Test logout.
        **Test Scenario:**
        #. Get login page
        #. Enter the correct username and password
        #. Press on "Login" button
        #. Check that login is done, Should succeed.
        #. Logout, Should succeed.
        """
        self.login(username=self.username, password=self.password)
        self.assertIn(self.username, self.get_text(element="greetings"))
        self.click(element="logout")
        self.assertEqual('Login', self.get_text(element="login_submit"))

