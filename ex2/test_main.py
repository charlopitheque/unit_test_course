import sys
import unittest

# sys.path.append('C:\\Ynov\\tests_unitaires\\assenceur')
from main import IsLeapYear


class TestLeapYearV1(unittest.TestCase):

    def test_is_leap_year_v1(self):
        test_ex = IsLeapYear()
        self.assertEqual(True, test_ex.is_leap_year_v1(2000))
        self.assertEqual(False, test_ex.is_leap_year_v1(2001))

    def test_is_leap_year_v1_exception(self):
        test_ex = IsLeapYear()
        with self.assertRaises(TypeError):
            test_ex.is_leap_year_v1("2001")


class TestLeapYearV2(unittest.TestCase):

    def test_is_leap_year_v2(self):
        test_ex = IsLeapYear()
        self.assertEqual(True, test_ex.is_leap_year_v1(2000))
        self.assertEqual(False, test_ex.is_leap_year_v1(2001))

    def test_is_leap_year_v2_exception(self):
        test_ex = IsLeapYear()
        with self.assertRaises(TypeError):
            test_ex.is_leap_year_v1("2001")


if __name__ == '__main__':
    unittest.main()
