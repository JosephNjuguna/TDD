import unittest
import revision_test

class TestRevision(unittest.TestCase):
    def test_word(self):
        result = revision_test.hello()# the main difference i
                                    #  wanted to test was here
        self.assertEqual("hello world", result)

    def test_string(self):
        word = "Andela"
        result = revision_test.string_test(word)
        self.assertEqual("Andela", result)

    def test_raise_errors(self):
        self.assertRaises(ValueError, revision_test.string_test, 23)
        
if __name__ == '__main__':
    unittest.main()
