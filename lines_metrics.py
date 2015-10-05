__author__ = 'liza'
from string_pars_functions_2 import word_count, tfidf, person_names, punctuation, question, line_sentence
from string_pars_functions import line_position, accent_vowels, ikt_schema, pos_stream
import codecs

def main():
    t = codecs.open('metrics_table.csv', 'w', 'utf-8')
    data = codecs.open('zhuk-all.txt', 'r', 'utf-8')
    line = ''

if __name__ == '__main__':
    main()
