class ComplexFunctions():
    def word(self):
        return "Helloo"

    def is_isogram(self, word):
        if type(word) != str:
            raise AssertionError('thats not a string')
        if word.strip()=='':
            return word,False
        else:
            if word and len(set(word)) == len(word):
                return word,True
            else:
                return word,False
