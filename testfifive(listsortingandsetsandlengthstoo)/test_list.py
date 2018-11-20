import unittest
import list_test

class Test(unittest.TestCase):
    def test_output(self):
        result1 = list_test.remove_duplicates('aaabbbac')
        result2 = list_test.remove_duplicates('a')
        result3 = list_test.remove_duplicates('thelexash')

        #total number of duplicates dropped
        #the new list that is made after the duplicates are dropped

        self.assertIsInstance(result1,tuple, msg = 'Incorrect Output type')
        self.assertEqual(result1, ('abc', 5) ,msg = 'Incorrect Output')

        self.assertIsInstance(result2,tuple, msg = 'Incorrect Output type')
        self.assertEqual(result2, ('a', 0) ,msg = 'Incorrect Output')

        self.assertIsInstance(result3,tuple, msg = 'Incorrect Output type')
        self.assertEqual(result3, ('aehlstx',2 ) ,msg = 'Incorrect Output')
if __name__ == '__main__':
    unittest.main()
