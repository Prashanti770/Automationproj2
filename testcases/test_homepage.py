import pytest
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from pages.loginpage import Loginpage
from utilities.readProperties import Readconfig
from pages.Homepage import Homepage

@pytest.mark.usefixtures("test_logintopage")
class Test_002_home():
    # lpc = Test_001_login.test_logintopage()
    # baseURL = Readconfig.getApplicationURL()
    # user = Readconfig.getUseremail()
    # pwd = Readconfig.getPassword()

    def get_product_info(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.home = Homepage(self.driver)
        #
        # # self.home = Homepage(self.lpc)
        # self.lp.setusername(self.user)
        # self.lp.setpassword(self.pwd)
        # self.lp.clicklogin()
        self.home.product_link
        self.home.product_text




