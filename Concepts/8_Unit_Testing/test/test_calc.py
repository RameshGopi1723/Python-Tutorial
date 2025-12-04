import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 20), 30)
        self.assertEqual(calc.add(10, 200), 210)

    def test_sub(self):
        self.assertEqual(calc.sub(10, 20), -10)
        self.assertEqual(calc.sub(10, 200), -190)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 20), 200)
        self.assertEqual(calc.multiply(10, 200), 2000)

    def test_division(self):
        self.assertEqual(calc.division(10, 5), 2)
        self.assertEqual(calc.division(10, 2), 5)

        self.assertRaises(ValueError, calc.division, 10, 0)

        # Context Manager - preferable for exception testing
        with self.assertRaises(ValueError):
            calc.division(10, 0)


if __name__ == "__main__":
    unittest.main()
