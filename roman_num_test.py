import unittest
from roman_num import roman_numeral

class TestRomanNumerals(unittest.TestCase):
    def test_If_Input_Is_Int(self):
        self.assertEqual("This is not a number", ValueError)
    def test_If_Input_Within_0_and_4000(self):
        self.assertEqual(4001, IndexError)
    def test_integer_to_roman_numeral(self):
        self.assertEqual(10, "X")
    
if __name__ == '__main__':
    unittest.main()
