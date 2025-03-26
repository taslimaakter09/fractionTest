import unittest
from fraction import Fraction

class TestFractionAdd(unittest.TestCase):
    """Tests for the __add__ method of Fraction class."""

    def setUp(self):
        self.f1 = Fraction(1, 2)
        self.f2 = Fraction(1, 3)
        self.f3 = Fraction(-1, 6)

    def test_add_positive(self):
        result = self.f1 + self.f2
        self.assertEqual(str(result), "5/6", "1/2 + 1/3 should be 5/6")

    def test_add_negative(self):
        result = self.f1 + self.f3
        self.assertEqual(str(result), "1/3", "1/2 + (-1/6) should be 1/3")

    def test_add_whole_number(self):
        result = Fraction(2) + Fraction(3, 4)
        self.assertEqual(str(result), "11/4", "2 + 3/4 should be 11/4")

    def test_add_invalid_type(self):
        with self.assertRaises(TypeError, msg="Adding a non-Fraction should raise TypeError"):
            _ = self.f1 + 1


if __name__ == '__main__':
    unittest.main()