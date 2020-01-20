import unittest
from roman_num import roman_numeral

class RomanNumeralsTest(unittest.TestCase):
    def TestIfInputIsInt(self):
        self.assertEqual("NotANumber", ValueError)

    def TestIfInputWithin0and4000(self):
        self.assertEqual(4001, ValueError)

if __name__ == '__main__':
    unittest.main()
