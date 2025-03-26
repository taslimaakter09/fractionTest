import unittest
from fraction import Fraction

class TestFractionStr(unittest.TestCase):
    """Tests for the __str__ method of Fraction class."""

    def test_str_simple(self):
        f = Fraction(3, 4)
        self.assertEqual(f.__str__(), "3/4", "String representation should be '3/4'")

    def test_str_negative(self):
        f = Fraction(-1, 2)
        self.assertEqual(f.__str__(), "-1/2", "String representation should be '-1/2'")

    def test_str_whole_number(self):
        f = Fraction(5, 1)
        self.assertEqual(f.__str__(), "5", "String representation should be '5' when denominator is 1")

    def test_str_reduce_to_whole_number(self):
        f = Fraction(4, 2)
        self.assertEqual(f.__str__(), "2", "Fraction(4,2) should reduce to whole number '2'")


if __name__ == '__main__':
    unittest.main()