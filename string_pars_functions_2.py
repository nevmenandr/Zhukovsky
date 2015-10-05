# coding: utf-8
__author__ = 'liza'

from tf_idf import compute_tfidf
import codecs, re
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
re_line = re.compile('>([^<]*)<br>')
uppercase = u'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
punct = ':.?!";'
punct_term = '.?!"…'
pers_names = set(line.strip() for line in codecs.open('person_names.txt', 'r', 'utf-8'))

text = codecs.open('zhuk-all.txt', 'r', 'utf-8')

corpus = [tokenizer.tokenize(re_line.findall(line.replace(u'`', ''))[0]) for line in text]

# line is a stream of tokens, corpus is a stream of lines

def word_count(line):
    return len(line)


def tfidf(line):
    tfidfs = compute_tfidf(line, corpus)
    return len([x for x in tfidfs if tfidfs[x] > 0.7])


def person_names(line):
    pers = [x for x in line if x[0] in uppercase]
    num_pers = 0
    for p in pers:
        if p in pers_names:
            num_pers += 1
    return num_pers


def punctuation(line):
    for word in line:
        if word in punct:
            return True
    return False


def question(line):
    for word in line:
        if '?' in word:
            return True
    return False

def line_sentence(line):
    if line[-1] in punct_term:
        return True
    else:
        return False

if __name__ == '__main__':
    pass