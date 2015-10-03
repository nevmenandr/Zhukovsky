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

def line_position(string):
    r = re.search(u'id="(\d+)" s="(.+?)"', string)
    line_num = int(r.group(1))
    song_num = r.group(2)
    partition = songs_num[song_num]
    prev = partition['begin']
    for indx, p_name in enumerate(parts_names):
        if indx == 0:
            continue
        if prev <= line_num <= partition[p_name]:
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



def main():
    
    return 0

if __name__ == '__main__':
    main()

