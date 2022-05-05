import pytest
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.base_driver import BaseDriver

class Loginpage(BaseDriver):

    user_text = "//input[@id='user-name']"
    password_text = "//input[@id='password']"
    login_click = "//input[@id='login-button']"
    home_logo = "//div[@class='bot_column']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def pagelogo(self):
        self.ec_wait(By.XPATH, self.home_logo).is_displayed()


    def setusername(self,username):
        # with pytest.raises(NoSuchElementException):
        # with pytest.raises(TimeoutException) as Excepinfo:
        # try:
        # self.wait_until_element_is_clickable(By.XPATH,self.user_text).clear()
        # self.wait_until_element_is_clickable(By.XPATH, self.user_text).send_keys(username)
        try :
            self.ec_wait(By.XPATH,self.user_text).clear()
            self.ec_wait(By.XPATH,self.user_text).send_keys(username)
        except TimeoutException as Excepinfo:
            print("")
            pytest.fail(Excepinfo)





    def setpassword(self,password):

        self.wait_until_element_is_clickable(By.XPATH,self.password_text).clear()
        self.wait_until_element_is_clickable(By.XPATH, self.password_text).send_keys(password)

    def clicklogin(self):
        self.wait_until_element_is_clickable(By.XPATH,self.login_click).click()

    # def logindetails(self,user,pwd):
    #
    #     self.setusername().clear()
    #     self.setusername().send_keys(user)
    #     self.setusername().send_keys(Keys.ENTER)
    #     self.setpassword().clear()
    #     self.setpassword().send_keys(pwd)
    #     self.setpassword().send_keys(Keys.ENTER)
    #     self.clicklogin().click()



