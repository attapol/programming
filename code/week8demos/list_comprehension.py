# -*- coding: utf-8 -*-

verbs = ['happen', 'add', 'pull', 'walk']

# first method
past_verbs = []
for verb in verbs:
    past_verb = verb + 'ed'
    past_verbs.append(past_verb)

# second method
past_verbs = [verb + 'ed' for verb in verbs]

# third method
past_verb_transform = lambda word: word + 'ed'
past_verbs = [past_verb_transform(verb) for verb in verbs]

# fourth method
def past_verb_transform_fn(word):
    return word + 'ed'

past_verbs = [past_verb_transform_fn(verb) for verb in verbs]

#fifth method
past_verbs = list(map(lambda word: word + 'ed', verbs))

