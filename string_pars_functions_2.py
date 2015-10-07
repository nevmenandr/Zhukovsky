# coding: utf-8
__author__ = 'liza'

from tf_idf import compute_tfidf
import codecs, re
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
re_line = re.compile('>([^<]*)<br>')
uppercase = u'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
punct = ':.?!";'
punct_term = u'.?!"…'
pers_names = set(line.strip() for line in codecs.open('person_names.txt', 'r', 'utf-8'))

text = codecs.open('zhuk-all.txt', 'r', 'utf-8')

corpus = [[word for word in tokenizer.tokenize(re_line.findall(line.replace(u'`', ''))[0]) if re.search(u'[А-Яа-я]', word)] for line in text]

# line is a stream of tokens, corpus is a stream of lines

def word_count(line):
    return len(line)

def word_count2(line):
    line = re.sub(u'<.+?>', u'', line)
    words = line.split()
    i_words = 0
    for word in words:
        if re.search(u'[А-Яа-я]', word):
            i_words += 1
    return i_words
    

def tfidf(line):
    tfidfs = compute_tfidf(line, corpus)
    return len([x for x in tfidfs if tfidfs[x] > 0.5])


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
            return 1
    return 0


def question(line):
    for word in line:
        if '?' in word:
            return 1
    return 0

def line_sentence(line):
    if line[-1] in punct_term:
        return 1
    else:
        return 0

if __name__ == '__main__':
    pass
