import unittest
from fraction import Fraction

class TestFractionSub(unittest.TestCase):
    """Tests for the __sub__ method of Fraction class."""

    def test_sub_positive(self):
        result = Fraction(3, 4) - Fraction(1, 4)
        self.assertEqual(str(result), "1/2", "3/4 - 1/4 should be 1/2")

    def test_sub_negative_result(self):
        result = Fraction(1, 4) - Fraction(3, 4)
        self.assertEqual(str(result), "-1/2", "1/4 - 3/4 should be -1/2")

    def test_sub_whole_number(self):
        result = Fraction(5) - Fraction(1, 2)
        self.assertEqual(str(result), "9/2", "5 - 1/2 should be 9/2")

    def test_sub_invalid_type(self):
        with self.assertRaises(TypeError, msg="Subtracting a non-Fraction should raise TypeError"):
            _ = Fraction(1, 2) - 1


if __name__ == '__main__':
    unittest.main()