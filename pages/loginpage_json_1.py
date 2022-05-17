import pytest
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.base_driver import BaseDriver
from ddt import file_data

class Loginpage(BaseDriver):

    user_text = "//input[@id='user-name']"
    password_text = "//input[@id='password']"
    login_click = "//input[@id='login-button']"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # @file_data("locators/login_locators.json")
    def setusername(self,username,password):
       self.wait_until_element_is_clickable(By.XPATH,self.user_text).clear()
       self.wait_until_element_is_clickable(By.XPATH,self.user_text).send_keys(username)
       self.wait_until_element_is_clickable(By.XPATH,self.password_text).clear()
       self.wait_until_element_is_clickable(By.XPATH, self.password_text).send_keys(password)
       self.wait_until_element_is_clickable(By.XPATH,self.login_click).click()





