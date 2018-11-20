import unittest
import ints_file

class Test(unittest.TestCase):
    def test_odds_even(self):
        list_num = [1,2,4,5,6]
        no = ints_file.my_sort(list_num)
        self.assertEqual([1,5,2,4,6], no)
if __name__ == '__main__':
    unittest.main()
