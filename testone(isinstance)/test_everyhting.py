import unittest
from self_test import Reminder

class TestMath(unittest.TestCase):
    def setUp(self):
        self.override = Reminder()

    def test_add (self):
        addition = self.override.ad(10,10)
        self.assertEqual(20 , addition)

    def test_subtraction(self):
        subtraction = self.override.minus(7,8)
        self.assertEqual(-1, subtraction)

    def test_division(self):
        divide= self.override.div(20,10)
        self.assertEqual(2, divide)

    def test_power(self):
        power = self.override.po(3,2)
        self.assertEqual(9,power)

    def test_custom_num_list(self):
        lnght = len(self.override.create_num_list(10))
        self.assertEqual(10,lnght)

    def test_calculator(self):
        result = self.override.addo(2,3)
        self.assertEqual(5,result)

    def test_calculator_return_error_if_both_args_are_not_numbers(self):
        self.assertRaises(ValueError, self.override.addo, 'two','three')

    def test_calculator_return_error_if_x_args_is_otnumber(self):
        self.assertRaises(ValueError, self.override.addo, 'four', 2)

    def test_calculator_return_error_if_y_args_is_otnumber(self):
        self.assertRaises(ValueError, self.override.addo, 2,'four')

if __name__ == '__main__':
    unittest.main()

"""
assertAlmostEqual(a,b) round() ==
assertNotAlmostEqual(a,b)   !=
assertGreater(a,b) | a>b
assertGreaterEqual(a,b) | a>=b
assertLess(a,b) | a<b
assertLessEqual(a,b) | a<=b
assertRegexpMatches( s, r ) | r.search(s)
assertNotRegexpMatches( s, r ) | not r.search(s)
assertItemsEqual(a, b) | sorted(a) == sorted(b)
assertDictContainsSubset(a, b) | all the key / value pairs in 'a'  exist in 'b'
"""
