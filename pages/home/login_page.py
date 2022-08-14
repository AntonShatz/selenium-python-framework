import time
from pages.home.navigation_page import NavigationPage
from base.basepage import BasePage

class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    def getTitle(self):
        return self.driver.title

    #Locators
    _login_link = "SIGN IN"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@value='Login']"
    _all_courses = "//a[@target='_self' and contains(text(),'ALL COURSES')]"

    def clickLoginLink(self):
        self.elementClick(self._login_link,locatorType="link")
    def enterEmail(self,email):
        self.sendKeys(email,self._email_field)
    def enterPassword(self,password):
        self.sendKeys(password,self._password_field)
    def clickLoginButton(self):
        self.elementClick(self._login_button,locatorType="xpath")

    def login(self,email="",password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        time.sleep(3)
        self.clickLoginButton()

    def verifyLoginSuccesful(self):
        result = self.isElementPresent("//h1[contains(text(),'My Courses')]",locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        time.sleep(5)
        result = self.isElementPresent("//span[contains(text(),'Your username or password is invalid. Please try a')]",locatorType="xpath")
        return result

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def verifyLoginTitle(self):
        return self.verifyPageTitle("My Courses")

    def LogOut(self):
        self.nav.navigateToMyCourses()
        self.elementClick(locator="//img[@class='zl-navbar-rhs-img ']",locatorType="xpath")
        self.elementClick(locator="//a[contains(text(),'Logout')]",locatorType="xpath")



