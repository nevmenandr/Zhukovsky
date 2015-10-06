# coding: utf-8
__author__ = 'liza'
import re
from string_pars_functions_2 import word_count, tfidf, person_names, punctuation, question, line_sentence
from string_pars_functions import line_position, accent_vowels, ikt_schema, pos_stream
import codecs, re
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
re_line = re.compile('>([^<]*)<br>')
uppercase = u'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
punct = ':.?!";'
punct_term = '.?!"…'
pers_names = set(line.strip() for line in codecs.open('person_names.txt', 'r', 'utf-8'))


def main():
    t = codecs.open('metrics_table.csv', 'w', 'utf-8')
    #t.write('id\tposition\twords_count\taccent_vowels\ttf_idf\tpos\tnames\tikt_schema\tpunctuation_in_the_middle\t' +
    #        'repetition\tquestion\tnegation\tline_sentence\tconj_constructions\n')
    text = codecs.open('zhuk-all-nacnt-lemm.txt', 'r', 'utf-8')
    lemmed_lines = {}
    for line in text:
        idr = re.search(u'<id="(\d+)"', line)
        if idr:
            line_id = int(idr.group(1))
            lemmed_lines[line_id] = line
    text.close()
    text = codecs.open('zhuk-all.txt', 'r', 'utf-8')
    primary_line_metrics = {}
    for line in text:
        idr = re.search(u'<id="(\d+)"', line)
        if idr:
            line_id = int(idr.group(1))
        line = line.strip()
        print line
        if u'#Гек6ж' not in line:
            ano = '1'
        else:
            ano = '0'
        line_arr = tokenizer.tokenize(re_line.findall(line.replace(u'`', ''))[0])
        position = line_position(line)
        words_count = str(word_count(line_arr))
        acc_v = accent_vowels(line)
        tf_idf = str(tfidf(line_arr))
        pos, num, s, v, a, adv, spro, pr, part, conj, intj = pos_stream(lemmed_lines[line_id])
        names = str(person_names(line_arr))
        ikt = ikt_schema(line)
        punct = str(punctuation(line_arr))
        #repetition =
        quest = str(question(line_arr))
        neg = str(negation(line))
        sent = str(line_sentence(line_arr))
        constr = str(ili(line))
        #table_line = str(line_id) + '\t' + words_count + '\t' + acc_v + '\t' + tf_idf + '\t' + pos + '\t' + names + '\t' + ikt + '\t' + punct +\
        #             '\t\t' + quest + '\t\t' + sent + '\t'
        primary_line_metrics[line_id] = [ano, words_count, acc_v, tf_idf, pos, names, ikt, punct, quest, sent, str(num), str(s), str(v), str(a), str(adv), str(spro), str(pr), str(part), str(conj), str(intj), constr]
        #t.write(table_line + '\n')
    t.close()

if __name__ == '__main__':
    main()
