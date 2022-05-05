import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.loginpage import Loginpage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen


# @pytest.mark.usefixtures("setup")
@allure.severity(allure.severity_level.NORMAL)
class Test_001_login():
    baseURL = Readconfig.getApplicationURL()
    user = Readconfig.getUseremail()
    pwd = Readconfig.getPassword()
    logger1 = LogGen.loginfo()



    # @pytest.mark.xfail(raises=TimeoutException)
    # @pytest.mark.xfail()

    # @staticmethod
    # @pytest.fixture()
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logintopage(self,setup):
        self.logger1.info("********* Test_001_login *********")
        # self.logger1.info("*************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger1.info("********* Open Loginpage  *********")
        self.lp = Loginpage(self.driver)
        # with pytest.raises() :
        # with pytest.raises(NoSuchElementException) as excinfo:
        # with pytest.raises(TimeoutException) as excinfo:


        # try:
        self.lp.setusername(self.user)
        self.lp.setpassword(self.pwd)
            # assert "Element not found" in str(excinfo.value)
            # assert "Element not found" in str(excinfo)
            # print(str)

        # except :
            # raise ValueError("Please check!!!!")
        # except TimeoutException :
        # except NoSuchElementException :
        #     print(e)
        #     pytest.fail("element not found here ")
        self.lp.clicklogin()
        self.logger1.info("********* Successfully login  into the page *********")
            # print("login successfull")
            # assert "Element not found" == str(excinfo.value)

        # except TimeoutException as excinfo:
        #     print(excinfo)
        self.driver.close()

    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self,setup):
        pytest.skip("Test case is skipped")
        self.driver.close()
        # self.logger1.info("********* Verify Homepage Logo *********")
        # self.driver = setup
        # self.driver.get(self.baseURL)
        # self.lp = Loginpage(self.driver)
        # status = self.lp.pagelogo()
        # if status == True:
        #     assert True
        # else:
        #     assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_hometitles(self,setup):

        self.logger1.info("********* Verify Homepage Title *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title


        if act_title == "Swag Labs 9":
            self.logger1.info("********* Title is correct *********")
            print("title is", act_title)

            self.driver.close()
            assert True

        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="Testcase01 title",attachment_type=AttachmentType.PNG)
            self.logger1.error("********* Title is incorrect *********")
            self.driver.save_screenshot(".\\Screenshots\\test_hometitle.png")
            self.driver.close()
            assert False



