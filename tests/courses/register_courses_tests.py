import unittest
from utilities.teststatus import TsStatus
from pages.courses.register_courses_pages import RegisterCoursesPage
import pytest
from ddt import ddt,data,unpack
from utilities.read_data import getCSVdata
from pages.home.navigation_page import NavigationPage

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self,oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TsStatus(self.driver)
        self.nav = NavigationPage(self.driver)


    def setUp(self):
        self.nav.navigateToAllCourses()


    @pytest.mark.run(order=3)
    @data(*getCSVdata("testdata.csv"))
    @unpack
    def test_invalidEnrollment(self,courseName,searchCourse,ccnum,ccexp,cccvv):
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(searchCourse)
        self.courses.enrollCourse(num=ccnum,exp=ccexp,cvv=cccvv)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment",result,"Enrollment Failed Varification")




