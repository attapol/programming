
def convert_date_format(date_str):
    """
    
    >>> convert_date_format('04/15/2011')
    '15 APR 2011'
    """
    split_date_str = date_str.split('/')
    month = split_date_str[0]
    day = split_date_str[1]
    year = split_date_str[2]
    months = ['JAN', 'FEB', 'MAR', 'APR']
    month_name = months[int(month) - 1]
    return '{} {} {}'.format(day, month_name, year)
    

def generate_bigram(words):
    bigram_list = []
    for i in range(len(words)):
        if (i + 1) < len(words):
            bigram = words[i] + '---' + words[i+1]
            bigram_list.append(bigram)
    return bigram_list


def convert_to_plural(word):
    return word + 'es' if word[-1] == 's' else word + 's'

import random
def coin_flip():
    if random.random() > 0.5:
        print ('HEAD')
    else:
        print ('TAIL')
        
def jump_words(text):
    words = text.split(' ')
    for i in range(len(words)):
        # หารสามลงตัว
        if i % 3 == 0:
            print (words[i])

import random    
def compose_random(word_list):
    random_words = []
    not_found_me = True
    while not_found_me:
        picked_word = random.choice(word_list)
        random_words.append(picked_word)
        not_found_me = picked_word != 'me'    
    return random_words        