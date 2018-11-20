def long_word(sentence):
    sentence = sentence.split()
    l_word = ''
    l_size = 0
    for n in sentence:
        if len(n) > l_size:
            l_word = n
            l_size = len(n)
        return l_word
