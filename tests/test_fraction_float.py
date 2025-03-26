import unittest
from fraction import Fraction

class TestFractionFloat(unittest.TestCase):
    """Tests for the __float__ method of Fraction class."""

    def test_float_default(self):
        value = Fraction().__float__()
        self.assertEqual(str(value), "0.0", "Default Fraction() should convert to 0.0")

    def test_float_simple(self):
        value = Fraction(1, 2).__float__()
        self.assertEqual(str(value), "0.5", "Fraction(1,2) should be 0.5")

    def test_float_negative(self):
        value = Fraction(-1, 4).__float__()
        self.assertEqual(str(value), "-0.25", "Fraction(-1,4) should be -0.25")

    def test_float_whole_number(self):
        value = Fraction(3).__float__()
        self.assertEqual(str(value), "3.0", "Fraction(3) should be 3.0")


if __name__ == '__main__':
    unittest.main()