import os
from utilities import login_locators_read as RJ
from base.base_driver import BaseDriver
class BasePage(BaseDriver):

    def __init__(self, driver):
        self.driver = driver

    def pageLocators(self, page):

        locatorsPath = os.path.abspath("./locators/login_locators.json")
        locatorsJsonFile = RJ.readJson(locatorsPath)
        pageLocators = [locator for locator in locatorsJsonFile if locator['pageName'] in page]
        return pageLocators

    def locator(self, pageLocators, locatorName):

        for locator in pageLocators:
            if locatorName == locator['name']:
                return locator['locator'], locator['locateUsing']

