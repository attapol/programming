import spacy

processor = spacy.load('en')
text = 'She sells seashells on the seashore'
document = processor(text)
token_list = list(document)
for token in token_list:
    print (token, token.pos_, token.tag_, token.lemma_)

