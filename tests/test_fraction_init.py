import unittest
from fraction import Fraction

class TestFractionInit(unittest.TestCase):
    """Tests for the __init__ method of Fraction class."""

    def test_default(self):
        f = Fraction()
        self.assertEqual(f.__str__(), "0/1", "Default Fraction() should be 0/1")

    def test_reduce_fraction(self):
        f = Fraction(2, 4)
        self.assertEqual(f.__str__(), "1/2", "Fraction(2,4) should reduce to 1/2")

    def test_whole_number(self):
        f = Fraction(5)
        self.assertEqual(f.__str__(), "5/1", "Fraction(5) should be represented as 5/1")

    def test_zero_numerator(self):
        f = Fraction(0, 5)
        self.assertEqual(f.__str__(), "0/1", "Fraction(0,5) should reduce to 0/1")

    def test_negative_numerator(self):
        f = Fraction(-3, 6)
        self.assertEqual(f.__str__(), "-1/2", "Fraction(-3,6) should reduce to -1/2")

    def test_both_negative(self):
        f = Fraction(-3, -6)
        self.assertEqual(f.__str__(), "1/2", "Fraction(-3,-6) should reduce to 1/2")

    def test_denominator_zero(self):
        with self.assertRaises(ZeroDivisionError, msg="Denominator=0 should raise ZeroDivisionError"):
            Fraction(3, 0)

    def test_invalid_type(self):
        with self.assertRaises(TypeError, msg="Fraction(2.4) should raise TypeError"):
            Fraction(2.4)


if __name__ == '__main__':
    unittest.main()
