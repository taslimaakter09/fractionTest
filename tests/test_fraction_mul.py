import unittest
from fraction import Fraction

class TestFractionMul(unittest.TestCase):
    """Tests for the __mul__ method of Fraction class."""

    def test_mul_positive(self):
        result = Fraction(2, 3) * Fraction(3, 4)
        self.assertEqual(str(result), "1/2", "2/3 * 3/4 should be 1/2")

    def test_mul_negative(self):
        result = Fraction(-1, 2) * Fraction(2, 3)
        self.assertEqual(str(result), "-1/3", "-1/2 * 2/3 should be -1/3")

    def test_mul_by_zero(self):
        result = Fraction(3, 4) * Fraction(0)
        self.assertEqual(str(result), "0", "Any fraction multiplied by 0 should be 0")

    def test_mul_invalid_type(self):
        with self.assertRaises(TypeError, msg="Multiplying by a non-Fraction should raise TypeError"):
            _ = Fraction(1, 2) * 2

if __name__ == '__main__':
    unittest.main()