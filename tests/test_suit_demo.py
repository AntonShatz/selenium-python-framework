import unittest
from tests.home.login_tests import LoginTests
from tests.courses.register_courses_tests import RegisterCoursesTests

# Get all tests from the tests classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesTests)

# Create a test suit combing all test classes
smokeTest = unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner(verbosity=2).run(smokeTest)