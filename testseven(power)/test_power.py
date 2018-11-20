import unittest
import powervalue

class TestPower(unittest.TestCase):
    def test_power(self):
        x,y= 3,3
        result = powervalue.techdead(x,y)
        self.assertEqual(27,result,  msg="Expected {} but got {}".format(27 , result))

    def test_when_y_is_O(self):
        self.assertRaises(AssertionError,powervalue.techdead, 3,0)
if __name__ == '__main__':
    unittest.main()
