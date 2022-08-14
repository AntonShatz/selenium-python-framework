import time

from base.basepage import BasePage
import utilities.custom_logger as cl
import logging

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    # Locators
    _search_box = "course"
    _submit_search = "//button[@type='submit']"
    _course = "//h4[@class='dynamic-heading' and contains(text(),'{0}')]"
    _all_courses ="course-list"
    _enroll_button = "//button[@class='dynamic-button btn btn-default btn-lg btn-enroll']"
    _cc_num ="//input[@aria-label='Credit or debit card number']"
    _cc_exp ="exp-date"
    _cc_cvv ="cvc"
    _dropDown="//select[@name='country-list']" #value = 104 for israel
    _submit_Buy_Button = "//button[@class='zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button']"
    _enroll_error_message ="//button[@class='zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button']"

    # Element Interactions
    def enterCourseName(self, name):
        self.sendKeys(name,locator=self._search_box,locatorType="name")
        self.elementClick(locator=self._submit_search,locatorType='xpath')


    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName),locatorType='xpath')

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button,locatorType='xpath')

    def enterCardNum(self,num):
        self.SwitchFrameByIndex(self._cc_num,locatorType="xpath")
        self.sendKeys(num,locator=self._cc_num,locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        self.SwitchFrameByIndex(locator=self._cc_exp,locatorType="name")
        self.sendKeys(exp,locator=self._cc_exp,locatorType="name")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        self.SwitchFrameByIndex(locator=self._cc_cvv,locatorType="name")
        self.sendKeys(cvv,locator=self._cc_cvv,locatorType="name")
        self.switchToDefaultContent()

    def clickEnrollBuyButton(self):
        self.elementClick(locator=self._submit_Buy_Button)

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num,exp,cvv)


    def verifyEnrollFailed(self):
        result = self.isEnabled(self._enroll_error_message,locatorType="xpath",info="Enroll Button")
        return not result


