import time

from base.basepage import BasePage

class NavigationPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    #Locators
    _Home = "//a[contains(text(),'HOME')]"
    _All_Courses = "//a[contains(text(),'ALL COURSES')]"
    _support = "//a[contains(text(),'SUPPORT')]"

    def navigateToMyCourses(self):
        self.elementClick(locator=self._Home,locatorType="xpath")
    def navigateToAllCourses(self):
        self.elementClick(locator=self._All_Courses,locatorType="xpath")
    def navigateToSupport(self):
        self.elementClick(locator=self._support,locatorType="xpath")
