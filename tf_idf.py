#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-09-12
# 
# TF-IDF это  term frequency-inverse document frequency или, ежели на великом и могучем, частотность терминов-обратная частотность документов
# Это простой и удобный способ оценить важность термина для какого-либо документа относительно всех остальных документов. Принцип такой — если слово встречается в каком-либо документе часто, при этом встречаясь редко во всех остальных документах — это слово имеет большую значимость для того самого документа.
# Слова, неважные для вообще всех документов, например, предлоги или междометия — получат очень низкий вес TF-IDF (потому что часто встречаются во всех-всех документах), а важные — высокий.

import collections
import math

def compute_tf(text):
#На вход берем текст в виде списка (list) слов
    #Считаем частотность всех терминов во входном массиве с помощью 
    #метода Counter библиотеки collections
    tf_text = collections.Counter(text)
    for i in tf_text:
        #для каждого слова в tf_text считаем TF путём деления
        #встречаемости слова на общее количество слов в тексте
        tf_text[i] = tf_text[i]/float(len(text))
    #возвращаем объект типа Counter c TF всех слов текста
    return tf_text

#text = ['hasta', 'la', 'vista', 'baby', 'la', 'vista', 'la']
#print compute_tf(text)
#Out: Counter({'la': 0.42857142857142855, 'vista': 0.2857142857142857,
#'hasta': 0.14285714285714285, 'baby': 0.14285714285714285})

def compute_idf(word, corpus):
#на вход берется слово, для которого считаем IDF
#и корпус документов в виде списка списков слов
        #количество документов, где встречается искомый термин
        #считается как генератор списков
        return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))
        
#texts = [['pasta', 'la', 'vista', 'baby', 'la', 'vista'],
#['hasta', 'siempre', 'comandante', 'baby', 'la', 'siempre'],
#['siempre', 'comandante', 'baby', 'la', 'siempre']]
#print compute_idf('pasta', texts)
#Out: 0.47712125472

############################################################
# the same:

def compute_tfidf(line, corpus):
    #documents_list = []
    #for text in corpus:
    tf_idf_dictionary = {}
    computed_tf = compute_tf(line)
    for word in computed_tf:
        tf_idf_dictionary[word] = computed_tf[word] * compute_idf(word, corpus)
    #    documents_list.append(tf_idf_dictionary)
    return tf_idf_dictionary

#corpus = [['pasta', 'la', 'vista', 'baby', 'la', 'vista'],
#['hasta', 'siempre', 'comandante', 'baby', 'la', 'siempre'],
#['siempre', 'comandante', 'baby', 'la', 'siempre']]
#print compute_tfidf(corpus)
#Out: [{'pasta': 0.11928031367991561, 'baby': 0.0, 'vista': 0.23856062735983122, 'la': 0.0},
#'hasta': 0.09542425094393249, 'comandante': 0.03521825181113625, 'siempre': 0.0704365036222725,
#'baby': 0.0, 'la': 0.0},
#{'comandante': 0.04402281476392031, 'baby': 0.0, 'siempre': 0.08804562952784062, 'la': 0.0}]

#def main():
    
#    return 0

#if __name__ == '__main__':
#    main()

#from sklearn.feature_extraction.text import TfidfVectorizer
#corpus = ["This is very strange",
          #"This is very nice"]
#vectorizer = TfidfVectorizer(min_df=1)
#X = vectorizer.fit_transform(corpus)
#idf = vectorizer.idf_
#print dict(zip(vectorizer.get_feature_names(), idf))
#Output:

#{u'is': 1.0,
 #u'nice': 1.4054651081081644,
 #u'strange': 1.4054651081081644,
 #u'this': 1.0,
 #u'very': 1.0}
#As discussed in the comments, prior to version 0.15, a workaround is to access the attribute idf_ via the supposedly hidden _tfidf (an instance of TfidfTransformer) of the vectorizer:

#idf = vectorizer._tfidf.idf_
#print dict(zip(vectorizer.get_feature_names(), idf))
