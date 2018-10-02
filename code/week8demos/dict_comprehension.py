#!/usr/bin/env python3
# -*- coding: utf-8 -*-

words = ['David', 'Germany', 'Zac', 'Emily', 'Mali']
name_type = ['PERSON', 'COUNTRY', 'PERSON', 'PERSON', 'COUNTRY']


# set comprehension
word_set = set(words)
word_set = {word for word in words if not word.endswith('y')}

word_to_name_type = dict(zip(words, name_type))

word_to_name_type = {}
for word, nt in zip(words, name_type):
    word_to_name_type[word] = nt.lower()
print(word_to_name_type)


word_to_name_type = {word:nt.lower() 
    for word, nt in zip(words, name_type) if not word.endswith('y')}
print (word_to_name_type)

