import unittest
from student import Student


class TestStudent(unittest.TestCase):

    @classmethod # this will run and show once at the beginning of the test
    def setUpClass(cls):
        print("setUpClass")


    @classmethod # this will run and show once at the end of the test
    def tearDownClass(cls):
        print("tearDownClass")

    # this will run and show after each test is run
    def tearDown(self):
        print("tearDown")

    # this will run and show before each test is run
    def setUp(self):
        print("setUp")
        self.student = Student("John", "Doe")

    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.student.full_name, "John Doe")

    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        print("test_email")
        self.assertEqual(self.student.email, "john.doe@email.com")


if __name__ == "__main__":
    unittest.main()
