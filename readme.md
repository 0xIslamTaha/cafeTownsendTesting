# cafetownsend Test suite
This is a full automation testing framework to cover the main functionality testing for cafetownsend project using **selenium** and **nosetests** frameworks. The tesing framework was designed to meet the **PageObjects** desing pattern. 

## Framework Structure:
```
.
├── cafeTownsendTesting.log
├── config.ini
├── readme.md
├── requirements.txt
├── testcases
│   ├── __init__.py
│   ├── test_a_logging.py
│   ├── test_b_create_employees.py
│   └── test_c_edit_delete_employees.py
└── utilize
    ├── base_test.py
    ├── elements.py
    └── __init__.py

```

## Pre-requestes:
- Python3, pip3
- Chrome (tested with Chromium  63.0.3239.84 Built on Ubuntu , running on Ubuntu 16.04)
- chromedriver (tested with version 2.33)


## Execution steps:
```bash
git clone https://github.com/islamTaha12/cafeTownsendTesting.git
cd cafeTownsendTesting
pip3 install -r requirements.txt
export PYTHONPATh='./'
nosetests-3.4 -sv --logging-level=WARNING --rednose --tc-file=config.ini testcases
```

## Latest execution report:
```bash
⇒  nosetests-3.4 -vs --rednose testcases --tc-file config.ini --logging-level WARNING
CAFEE-001 ... passed
CAFEE-002 ... passed
CAFEE-003 ... passed
CAFEE-004 ... passed
CAFEE-005 ... passed
CAFEE-006 ... passed
CAFEE-007 [with reason='empty', date=''] ... passed
CAFEE-007 [with reason='invalid_day_1', date='2017-10-00'] ... passed
CAFEE-007 [with reason='invalid_day_2', date='2017-1-09'] ... passed
CAFEE-007 [with reason='invalid_day_3', date='2017-20-01'] ... passed
CAFEE-007 [with reason='invalid_day_4', date='2017-02-31'] ... passed
CAFEE-008 ... passed
CAFEE-009 ... passed
CAFEE-010 ... passed
CAFEE-011 ... FAILED
CAFEE-012 ... passed
CAFEE-013 ... passed
======================================================================
1) FAIL: CAFEE-010
----------------------------------------------------------------------
   Traceback (most recent call last):
    testcases/test_c_edit_delete_employees.py line 80 in test003_edit_user_with_invalid_date
      self.assertTrue(self.check_element_is_exist(element='back'), " [x] Update should fail!")
   AssertionError: False is not true :  [x] Update should fail!

-----------------------------------------------------------------------------
17 tests run in 333.663 seconds. 
1 FAILED (16 tests passed)

```

## BUGS:
### bug001:
**Bug descriptiion**

Admin can update user data with invaild start date.

**Related test case**
```
        """ CAFEE-011

        * Edit user with invalid date.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with valid data, should succeed.
        #. Edit user with invalid date, should fail.
        """
```

**Command to execute this test case**
```bash
cd cafeTownsendTesting
export PYTHONPATh='./'
nosetests-3.4 -sv --logging-level=WARNING --rednose --tc-file=config.ini testcases/test_c_edit_delete_employees.py:UpdateEmployeesTestCases.test004_delete_user_from_main_page
```

## Test Cases:
This test suite support auto generate docs using sphynix tool.

here is the last of the test cases:

```
        """ CAFEE-001

        * Test login with provider credential.
        **Test Scenario:**
        #. Get login page
        #. Enter the correct username and password
        #. Press on "Login" button
        #. Check that login is done, Should succeed.
        """

        """ CAFEE-002

        * Test login with random credential.
        **Test Scenario:**
        #. Get login page
        #. Enter the random username and password
        #. Press on "Login" button
        #. Check that login is failed, Should succeed.
        """

        """ CAFEE-003

        * Test logout.
        **Test Scenario:**
        #. Get login page
        #. Enter the correct username and password
        #. Press on "Login" button
        #. Check that login is done, Should succeed.
        #. Logout, Should succeed.
        """

        """ CAFEE-004

        * Crete new user with valid data.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with valid data, should succeed.
        """

        """ CAFEE-005

        * Crete new user with empty first name.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with empty first name, should fail.
        """

        """ CAFEE-006

        * Crete new user with empty last name.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with empty last name, should fail.
        """

        """ CAFEE-007

        * Crete new user with invalid email.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with invalid date, should fail.
        """

        """ CAFEE-008

        * Crete new user with empty last name.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with empty email, should fail.
        """

        """ CAFEE-009

        * Edit user with valid data.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with valid data, should succeed.
        #. Edit user with valid data, should succeed.
        """

        """ CAFEE-010

        * Edit user with invalid data.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with valid data, should succeed.
        #. Edit user with invalid name, should fail.
        """

        """ CAFEE-011

        * Edit user with invalid date.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with valid data, should succeed.
        #. Edit user with invalid date, should fail.
        """

        """ CAFEE-012

        * Delete user from the main page.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with valid data, should succeed.
        #. Delete this new user, should succeed.
        """

        """ CAFEE-013

        * Delete user from the edit page.
        **Test Scenario:**
        #. Login to the system
        #. Create a user with valid data, should succeed.
        #. Go to the edit page.
        #. Delete user, should succeed.
        """

```
