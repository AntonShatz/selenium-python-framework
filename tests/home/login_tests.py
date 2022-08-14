from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TsStatus

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def ClassSetup(self,oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TsStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("atn505@gmail.com","13241324")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1,"Title correct")
        result2 = self.lp.verifyLoginSuccesful()
        self.ts.markFinal("test_validaLogin",result2," Login was not successful")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.LogOut()
        self.lp.login("atn505@gmail.com","132413244")
        result = self.lp.verifyLoginFailed()
        assert result == True




