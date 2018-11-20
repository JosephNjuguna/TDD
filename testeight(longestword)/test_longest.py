import unittest
import longest

class TestLongest(unittest.TestCase):
    def test_longest(self):
        word = "this is Andela"
        result = longest.long_word(word)
        self.assertEqual("Andela", result, msg="expected message is{} but got {}".format("Andela",result))

    def test_one_word(self):
        sentence = 'THIS'
        result = longest.long_word(sentence)
        self.assertEqual("THIS",result )
        
if __name__ == '__main__':
    unittest.main()
