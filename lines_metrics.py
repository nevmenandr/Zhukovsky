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

window = 3

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
    #t = codecs.open('metrics_table_no_context.tsv', 'w', 'utf-8')
    #t.write('id\tanomalia\tposition\twords_count\taccent_vowels\ttf_idf\tpos\tnames\tikt_schema\tpunctuation_in_the_middle\t' +
            #'question\tnegation\tline_sentence\tnumerals\tsubject\tverbs\tandjectives\tadverbs\tpersonal_pronomen\tprepositions\tpart\tconjunction\tinterjection\tconj_constructions\n')
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
        #t.write(str(line_id) + '\t' + table_line + '\n')
    #t.close()
    t = codecs.open('metrics_table_with_context_' + str(window) + '.csv', 'w', 'utf-8')
    t.write('id\tanomalia\tposition\twords_count\taccent_vowels\ttf_idf\tpos\tnames\tikt_schema\tpunctuation_in_the_middle\tquestion\tnegation\tline_sentence\tnumerals\tsubject\tverbs\tandjectives\tadverbs\tpersonal_pronomen\tprepositions\tpart\tconjunction\tinterjection\tconj_constructions\tprev_word_count\tprev_accent_vowels\tprev_tf_idf\tprev_names\tprev_punctuantion_in_the_middle\tprev_question\tprev_negation\tprev_line_sentence\tprev_numerals\tprev_subject\tprev_verbs\tprev_andjectives\tprev_adverbs\tprev_personal_pronomen\tprev_prepositions\tprev_part\tprev_conjunction\tprev_interjection\tprev_conj_constructions\tpost_word_count\tpost_accent_vowels\tpost_tf_idf\tpost_names\tpost_punctuantion_in_the_middle\tpost_question\tpost_negation\tpost_line_sentence\tpost_numerals\tpost_subject\tpost_verbs\tpost_andjectives\tpost_adverbs\tpost_personal_pronomen\tpost_prepositions\tpost_part\tpost_conjunction\tpost_interjection\tpost_conj_constructions\n')
    for line_id in primary_line_metrics:
        arr_metrics = primary_line_metrics[line_id]
        arr_metrics = context(arr_metrics, 'prev')
        arr_metrics = context(arr_metrics, 'forw')
        table_line = u'\t'.join(arr_metrics)
        t.write(str(line_id) + '\t' + table_line + '\n')
    t.close()

def context(arr_metrics, direction):
    prev_word_count = 0
    prev_acc_v = u''
    prev_tf_idf = 0
    prev_names = 0
    prev_punkt = 0
    prev_quest = 0
    prev_neg = 0
    prev_sent = 0
    prev_num = 0
    prev_s = 0
    prev_v = 0
    prev_a = 0
    prev_adv = 0
    prev_spro = 0
    prev_pr = 0
    prev_part = 0
    prev_conj = 0
    prev_intj = 0
    prev_constr = 0
    for x in range(1, window + 1):
        if direction == 'prev':
            if line_id - x > 0:
                prev_line = primary_line_metrics[line_id - x]
            else:
                break
        elif direction == 'forw':
            if line_id + x <= len(primary_line_metrics):
                prev_line = primary_line_metrics[line_id + x]
            else:
                break
            
            prev_word_count += int(prev_line[2])
            prev_acc_v += prev_line[3]
            prev_tf_idf += int(prev_line[4])
            prev_names += int(prev_line[6])
            prev_punkt += int(prev_line[8])
            prev_quest += int(prev_line[9])
            prev_neg += int(prev_line[10])
            prev_sent += int(prev_line[11])
            prev_num += int(prev_line[12])
            prev_s += int(prev_line[13])
            prev_v += int(prev_line[14])
            prev_a += int(prev_line[15])
            prev_adv += int(prev_line[16])
            prev_spro += int(prev_line[17])
            prev_pr += int(prev_line[18])
            prev_part += int(prev_line[19])
            prev_conj += int(prev_line[20])
            prev_intj += int(prev_line[21])
            prev_constr += int(prev_line[22])
            
    prev_array = [str(prev_word_count), prev_acc_v, str(prev_tf_idf), str(prev_names), str(prev_punkt), str(prev_quest), str(prev_neg), str(prev_sent), str(prev_num), str(prev_s), str(prev_v), str(prev_a), str(prev_adv), str(prev_spro), str(prev_pr), str(prev_part), str(prev_conj), str(prev_intj), str(prev_constr)]
    arr_metrics.extend(prev_array)
    return arr_metrics
                
        

if __name__ == '__main__':
    main()
