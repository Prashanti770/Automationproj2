import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.loginpage_json import LoginPage_json
from utilities.readProperties import Readconfig
from utilities.customLogger import customLogger


# @pytest.mark.usefixtures("setup")
@allure.severity(allure.severity_level.NORMAL)
class Test_001_login():
    baseURL = Readconfig.getApplicationURL()
    user = Readconfig.getUseremail()
    pwd = Readconfig.getPassword()
    logger1 = customLogger()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_logintopage(self,setup):
        self.logger1.info("********* Test_001_login *********")
        # self.logger1.info("*************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger1.info("********* Open Loginpage  *********")
        self.lp = LoginPage_json(self.driver)
        self.lp.login(self.user,self.pwd)

        self.logger1.info("********* Successfully login  into the page *********")






