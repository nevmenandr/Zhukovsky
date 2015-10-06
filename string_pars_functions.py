#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-10-04
# 

import re
import json

fsongs = open('songs_number.json')
songs_num = json.load(fsongs)
fsongs.close()

parts_names = ['begin', 'p1', 'p2', 'mid', 'p4', 'end']

jot = {u'ё': u'о',
    u'ю': u'у',
    u'я': u'а',
    u'е': u'э'}
    
pos_alias = {u'NUM': u'D',
    u'V': u'V',
    u'S': u'S',
    u'ADV': u'B',
    u'ADVPRO': u'M',
    u'A': u'A',
    u'SPRO': u'M',
    u'APRO': u'M',
    u'PR': u'P',
    u'PART': u'R',
    u'ANUM': u'D',
    u'INTJ': u'I',
    u'CONJ': u'C'}

def line_position(string):
    r = re.search(u'id="(\d+)" s="(.+?)"', string)
    line_num = int(r.group(1))
    song_num = r.group(2)
    partition = songs_num[song_num]
    prev = partition['begin']
    for indx, p_name in enumerate(parts_names):
        #print line_num, prev, partition[p_name]
        if indx == 0:
            continue
        if prev <= line_num < partition[p_name]:
            part = p_name
            break
        else:
            prev = partition[p_name]
    return part
    
def accent_vowels(string):
    string = string.lower()
    vowel_string = u''
    for indx, sym in enumerate(string):
        if sym == '`':
            vowel_string += string[indx - 1]
    return vowel_string
            
def ikt_schema(string):
    r = re.search(u'"><#(.+?) ([0-4*]+)>', string)
    schema = r.group(1)
    return schema

def pos_stream(string):
    string = re.sub(u'<.+?>', u'', string)
    anals = string.split('}')
    pos_string = ''
    num = 0
    s = 0
    v = 0
    a = 0
    adv = 0
    spro = 0
    pr = 0
    part = 0
    conj = 0
    intj = 0
    for ana in anals:
        r = re.search(u'=([A-Z]+?)(=|,)', ana)
        if r:
            pos = r.group(1)
            if pos in pos_alias:
                posa = pos_alias[pos]
                pos_string += posa
            if pos == 'NUM':
                num += 1
            elif pos == 'S':
                s += 1
            elif pos == 'V':
                v += 1
            elif pos == 'A':
                a += 1
            elif pos == 'ADV':
                adv += 1
            elif pos == 'SPRO':
                spro += 1
            elif pos == 'PR':
                pr += 1
            elif pos == 'PART':
                part += 1
            elif pos == 'CONJ':
                conj += 1
            elif pos == 'INTJ':
                intj += 1
    return pos_string, num, s, v, a, adv, spro, pr, part, conj, intj
            
def negation(string):
    string = re.sub(u'<.+?>', u'', string)
    neg = 0
    words = string.split()
    for word in words:
        word = words.strip()
        if word == u'не':
            neg += 1
        elif word == u'ни':
            neg += 1
        elif word == u'без':
            neg += 1
    return neg
    
def ili(string):
    string = re.sub(u'<.+?>', u'', string)
    neg = 0
    words = string.split()
    for word in words:
        word = words.strip()
        if word == u'или':
            return 1
        elif word == u'иль':
            return 1
    return 0

def main():
    return 0

if __name__ == '__main__':
    main()

