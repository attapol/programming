#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:47:01 2018

@author: te
"""
import spacy
import collections

class CorpusAnalyzer:
    
    def __init__(self, file_name, language, processor):
        self.file_name = file_name
        self.language = language
        self.processor = processor
        data_file = open(file_name)
        self.sentences = []
        for line in data_file:
            self.sentences.append(list(self.processor(line.strip())))
    
    def get_num_sentences(self):
        return len(self.sentences)
    
    
    def get_most_common_tag(self):
        pos_counter = collections.Counter()
        for sentence in self.sentences:
            for word in sentence:
                pos_counter[word.tag_] += 1
        return pos_counter.most_common()
                
        