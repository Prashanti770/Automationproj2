import pytest
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.base_driver import BaseDriver
from loginpage import Loginpage

class Homepage(BaseDriver):
    # lpc = Loginpage.login_click()
    product_link="//a[@id='item_4_title_link']"
    product_text="//div[@class='inventory_details_name large_size']"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def product_link_click(self):
        self.wait_until_element_is_clickable(By.XPATH,self.product_link).click()

    def get_product_text(self,text):
        product_text=self.wait_until_element_is_clickable(By.XPATH,self.product_text)
        print(product_text.text)





