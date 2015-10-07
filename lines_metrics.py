# coding: utf-8
__author__ = 'liza'
import re
import sys
from string_pars_functions_2 import word_count, tfidf, person_names, punctuation, question, line_sentence, word_count2
from string_pars_functions import line_position, accent_vowels, ikt_schema, pos_stream, negation, ili
import codecs, re
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
re_line = re.compile('>([^<]*)<br>')
uppercase = u'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
punct = ':.?!";'
punct_term = '.?!"…'
pers_names = set(line.strip() for line in codecs.open('person_names.txt', 'r', 'utf-8'))

def clean(line):
    line = re.sub(u'<.+?>', u'', line)
    line = line.replace(u'`', '')
    words = line.split()
    true_words = []
    for word in words:
        if re.search(u'[А-Яа-я]', word):
            true_words.append(word)
    return true_words

def main():
    t = codecs.open('metrics_table_no_context.tsv', 'w', 'utf-8')
    t.write('id\tanomalia\tposition\twords_count\taccent_vowels\ttf_idf\tpos\tnames\tikt_schema\tpunctuation_in_the_middle\t' +
            'question\tnegation\tline_sentence\tnumerals\tsubject\tverbs\tandjectives\tadverbs\tpersonal_pronomen\tprepositions\tpart\tconjunction\tinterjection\tconj_constructions\n')
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
        sys.stdout.write(line + '\n')
        if u'#Гек6ж' not in line:
            ano = '1'
        else:
            ano = '0'
        line_arr = [word for word in tokenizer.tokenize(re_line.findall(line.replace(u'`', ''))[0]) if re.search(u'[А-Яа-я]', word)]
        #line_arr = clean(line)
        position = line_position(line)
        words_count = str(word_count(line_arr))
        #words_count = str(word_count2(line))
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
        primary_line_metrics[line_id] = [ano, position, words_count, acc_v, tf_idf, pos, names, ikt, punct, quest, neg, sent, str(num), str(s), str(v), str(a), str(adv), str(spro), str(pr), str(part), str(conj), str(intj), constr]
        table_line = u'\t'.join(primary_line_metrics[line_id])
        t.write(str(line_id) + '\t' + table_line + '\n')
    t.close()
    #t = codecs.open('metrics_table_with_context.csv', 'w', 'utf-8')
    #for line_id in primary_line_metrics:
        
        #primary_line_metrics[line_id]
        

if __name__ == '__main__':
    main()
