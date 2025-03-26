import unittest
from fraction import Fraction

class TestFractionDiv(unittest.TestCase):
    """Tests for the __truediv__ method of Fraction class."""

    def test_div_positive(self):
        result = Fraction(3, 4) / Fraction(1, 2)
        self.assertEqual(str(result), "3/2", "3/4 / 1/2 should be 3/2")

    def test_div_negative(self):
        result = Fraction(-1, 2) / Fraction(1, 4)
        self.assertEqual(str(result), "-2", "-1/2 / 1/4 should be -2")

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError, msg="Division by zero should raise ZeroDivisionError"):
            _ = Fraction(1, 2) / Fraction(0, 1)

    def test_div_invalid_type(self):
        with self.assertRaises(TypeError, msg="Dividing by a non-Fraction should raise TypeError"):
            _ = Fraction(1, 2) / 2


if __name__ == '__main__':
    unittest.main()