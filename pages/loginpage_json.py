from selenium.webdriver.common.by import By

from base.basepage_json import BasePage

class LoginPage_json(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.loginPage_locators = self.pageLocators('LoginPage_json')


    def login(self, user, password):
        self.sendKeys(user, *self.locator(self.loginPage_locators, 'user_text'))
        self.sendKeys(password, *self.locator(self.loginPage_locators, 'password_text'))
        self.elementClick(*self.locator(self.loginPage_locators, 'login_click'))
