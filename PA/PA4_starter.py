import spacy

def learn_dictionary(word_list_file_name, en_data_file_name, 
        foreign_data_file_name, output_file_name):
    """Learn a dictionary from a given parallel corpus
    
    >>> learn_dictionary('word_list.txt', 'europarl-v7.de-en.en', 'europarl-v7.de-en.de', 'de_to_en_dict.tsv')
    """

def tag_data_file(model_file_name, data_file_name, output_file_name):
    """Tag data with POS tag

    Refer to https://attapol.github.io/programming/code/use_spacy.py
    for basic use of spacy
    >>> tag_data_file('en', 'europarl-v7.de-en.en', 'europarl-v7.de-en.tagged.en')
    """
    # disable sentence tree parser and name detector to improve speed
    processor = spacy.load(model_file_name, disable=['parser', 'ner'])
    


def learn_dictionary_pos(word_list_file_name, en_tagged_data_file_name, 
        foreign_tagged_data_file_name, output_file_name):
    """Learn a dictionary from a given tagged parallel corpus

    >>> learn_dictionary('word_list.txt', 'europarl-v7.de-en-tagged.en',
            'europarl-v7.de-en-tagged.de', 'de_to_en_dictv2.tsv')
    """

def translate_file(foreign_to_en_dictionary_file_name, foreign_sentence_file_name):
    """Translate sentences using the provided dictionary

    >>> translate_file('de_to_en_dict.tsv', 'de_sentences.txt')
    I am a Berliner .
    The parliament calls good men .
    """

def translate_interactive(foreign_to_en_dictionary_file_name):
    """Translate interactively

    The user can type in a sentence to translate.
    The program exits when the user enters an empty string. 

    >>> translate_interactive('de_to_en_dict.tsv'):
    Enter a sentence to translate: 
    """

if __name__ == '__main__':
    # You should keep changing this part to test/run your programs
    learn_dictionary('word_list.txt', 'europarl-v7.de-en.en',
            'europarl-v7.de-en.de', 'de_to_en_dict.tsv')
    tag_data_file('en', 'europarl-v7.de-en.en', 'europarl-v7.de-en.tagged.en')

