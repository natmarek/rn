import roman
import unittest

class TestRomanNumerals(unittest.TestCase):
    values = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))

    def test_to_roman_values(self):
        for integer, numeral in self.values:
            result = roman.to_roman(integer)
            self.assertEqual(numeral, result)

    def test_If_Input_Within_0_and_4000(self):
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, 4000)
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, 0)
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, 10000)

    def test_not_integer(self):
        self.assertRaises(roman.NotIntegerError, roman.to_roman, 1.0)

