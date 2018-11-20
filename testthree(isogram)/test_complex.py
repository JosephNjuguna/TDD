import unittest
from complex_test import ComplexFunctions

class TestAndelaTest(unittest.TestCase):
    def setUp(self):
        self.testing = ComplexFunctions()

    def test_the_funtion(self):
        self.assertEqual("Helloo",self.testing.word())

    def test_isogram(self):
        word = "joseph"
        result = self.testing.is_isogram(word)
        self.assertEqual((word ,True), result ,msg = "Isogram '{}' not detected correctly" . format(word))

    def test_checking_isogram(self):
        self.assertRaises(AssertionError, self.testing.is_isogram, (23 ,False))

    def test_check_isogram(self):
        self.assertRaises(AssertionError, self.testing.is_isogram, ("" ,False))

if __name__ == '__main__':
    unittest.main()

#ValueError
#AssertionError
#TypeError
#ZeroDivisionError
#AtrributError
#print("types %s AND %s " %(self.format, self.word))
