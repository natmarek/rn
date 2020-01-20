import unittest
from roman_num import roman_numeral

class TestRomanNumerals(unittest.TestCase):
    def test_If_Input_Is_Int(self):
        self.assertEqual(roman_numeral(0),0)
    def test_IfInputWithin0and4000(self):
        self.assertEqual(4001, IndexError)
    
if __name__ == '__main__':
    unittest.main()
