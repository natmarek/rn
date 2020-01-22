import unittest
from roman import Roman

class TestRomanNumerals(unittest.TestCase):
    def test_If_Input_Is_Int(self):
        self.assertEqual(int_to_roman(input("not int")), TypeError)

    def test_If_Input_Within_0_and_4000(self):
        self.assertEqual(int_to_roman(input(4002)), ValueError)

    def test_integer_to_roman_numeral(self):
        self.assertEqual(int_to_roman(input("10")), "X")
    
if __name__ == '__main__':
    unittest.main()
