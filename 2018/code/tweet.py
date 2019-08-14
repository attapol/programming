#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:31:13 2018

@author: te
"""
tweet = {
        'id': 'attapol',
        'text': 'I had a big lunch today.',
        'coordinate': (13.5, -12.5)
        }

tweet2 = {
        'id': 'iampeter',
        'text': 'I had a big dinner today.',
        'coordinate': (11.5, -10.5)
        }

def get_tweet_word_count(t):
    return len(t['text'].split(' '))

class Tweet:
    
    #class constant
    MAX_CHARS = 140 
    
    #Constructor
    def __init__(self, twitter_id, text, coordinate):
        #properties
        print ("I'm building a new tweet.")
        self.twitter_id = twitter_id
        self.text = text
        self.coordinate = coordinate
        
    def get_tweet_word_count(self):
        return len(self.text.split(' '))
    
    def get_character_count(self):
        return len(t.text)
    
    @classmethod
    def cut_off_like_tweet(cls, text_string):
        return text_string[0:cls.MAX_CHARS]