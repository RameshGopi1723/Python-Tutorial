import unittest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from employee import Employee


class Test_Employee(unittest.TestCase):
    def setUp(self):
        print("\nsetUp")
        self.emp1 = Employee("Gopinath", "R", 320000)
        self.emp2 = Employee("Himetha", "G", 34000)
        self.emp3 = Employee("Deepak", "R", 44000)

    def tearDown(self):
        print("tearDown\n")
        pass

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp1.email, "Gopinath.R@gmail.com")

        self.emp1.last = "Ramesh"
        self.assertEqual(self.emp1.email, "Gopinath.Ramesh@gmail.com")

    def test_full_name(self):
        print("tets_full_name")
        self.assertEqual(self.emp2.full_name, "Himetha G")

        self.emp2.last = "Gopinath"
        self.assertEqual(self.emp2.full_name, "Himetha Gopinath")

    def test_hike(self):
        print("test_hike")
        self.emp3.hike()
        self.emp1.hike()
        self.emp2.hike()

        self.assertEqual(self.emp3.pay, 690800.0)
        self.assertEqual(self.emp2.pay, 533800)
        self.assertEqual(self.emp1.pay, 5024000)

    def test_monthly_schedule(self):
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp1.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/R/June")
            self.assertEqual(schedule, "Success")

            mocked_get.return_value.ok = False
            schedule = self.emp2.monthly_schedule("November")
            mocked_get.assert_called_with("http://company.com/G/November")
            self.assertEqual(schedule, "Bad Request!")


if __name__ == "__main__":
    unittest.main()
