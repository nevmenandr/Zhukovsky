__author__ = 'liza'

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')


def word_count(line):
    return len(tokenizer.tokenize(line))