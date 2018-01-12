import unittest, time, uuid, random, logging
from selenium import webdriver
from testconfig import config
from termcolor import colored
from utilize.elements import elements
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseTest(unittest.TestCase):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('cafeTownsendTesting.log')
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = config['main']['url']
        self.username = config['main']['username']
        self.password = config['main']['password']
        self.browser = config['main']['browser']
        self.elements = elements
        self.logger = BaseTest.logger

    def setUp(self):
        self.driver = self.set_browser()
        self.driver.implicitly_wait(20)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(url=self.url)
        self.driver.maximize_window()
        self.logger.info(self._testMethodName)

    def tearDown(self):
        self.driver.quit()

    def set_browser(self):
        if self.browser == 'chrome':
            driver = webdriver.Chrome()
        elif self.browser == 'firefox':
            driver = webdriver.Firefox()
        elif self.browser == 'ie':
            driver = webdriver.Ie()
        elif self.browser == 'opera':
            driver = webdriver.Opera()
        elif self.browser == 'safari':
            driver = webdriver.Safari
        else:
            print(colored(" [x] Invalid browser configuration [%s]" % self.browser, 'red'))
            driver = webdriver.Chrome()
        return driver

    def wait_until_element_located(self, element):
        method = self.elements[element][0]
        value = self.elements[element][1]
        for temp in range(3):
            try:
                self.wait.until(EC.visibility_of_element_located((getattr(By, method), value)))
                return True
            except:
                time.sleep(1)
        else:
            return False

    def find_element(self, element):
        method = self.elements[element][0]
        value = self.elements[element][1]
        element_value = self.driver.find_element(getattr(By, method), value)
        return element_value

    def set_text(self, element, value):
        self.wait_until_element_located(element)
        self.find_element(element).clear()
        self.find_element(element).send_keys(value)

    def click(self, element):
        for temp in range(3):
            try:
                self.find_element(element).click()
                break
            except:
                time.sleep(1)
        else:
            print(colored(" [x] Can't find %s element" % element), 'red')

    def get_text(self, element):
        time.sleep(0.5)
        for temp in range(10):
            try:
                return self.find_element(element).text
            except:
                time.sleep(0.5)
        else:
            print(colored(" [x] 'NoSuchElementException(%s)" % element), 'red')

    def wait_element(self, element):
        if self.wait_until_element_located(element):
            return True
        else:
            return False

    def check_element_is_exist(self, element):
        if self.wait_element(element):
            return True
        else:
            return False

    def get_url(self):
        return self.driver.current_url

    def random_str(self):
        data = str(uuid.uuid4()).replace('-', '')
        return data[:random.randint(1, 10)]

    def random_date(self):
        date = "%d-%02d-%02d" % (random.randint(1990, 2017), random.randint(1, 12), random.randint(1, 30))
        return date

    def random_email(self):
        return "%s@gmail.com" % self.random_str()

    def login(self, username, password):
        self.set_text(element='login_username', value=username)
        self.set_text(element='login_password', value=password)
        self.click(element="login_submit")

    def create_new_user(self, first_name, last_name, start_date, email, add_user=True):
        self.click(element='create_user')
        self.set_text(element="first_name", value=first_name)
        self.set_text(element="last_name", value=last_name)
        self.set_text(element="start_date", value=start_date)
        self.set_text(element="email", value=email)
        if add_user:
            self.click(element="add_user")
        else:
            self.click(element="cancel_user")
        time.sleep(3)

    def is_user(self, username):
        time.sleep(3)
        return username in self.get_text(element='employee_list')

    def select_user(self, username):
        employees_list = self.get_text(element="employee_list")
        if username in employees_list:
            employees_list_items = self.driver.find_elements_by_tag_name('li')
            for item in employees_list_items:
                if item.text == username:
                    item.click()
                    return True
        return False

    def delete_user(self, username):
        time.sleep(2)
        if self.select_user(username=username):
            self.click('delete_user')
            alert = self.driver.switch_to_alert()
            alert.accept()

    def edit_user(self, old_username, **kwargs):
        if self.select_user(username=old_username):
            self.click(element="edit_user")
            for key in kwargs.keys():
                self.set_text(element=key, value=kwargs[key])
            self.click(element="update")

    def delete_user_from_edit_page(self, username):
        time.sleep(2)
        if self.select_user(username=username):
            self.click(element='edit_user')
            self.click(element='delete_user_2')
            alert = self.driver.switch_to_alert()
            alert.accept()
