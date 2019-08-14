#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# add s 
verbs = ['happen', 'add', 'pull', 'walk', 'miss', 'press']

# method 1
new_verb_list = []
for verb in verbs:
    if not verb.endswith('s'):
        new_verb_list.append(verb)

# method 2
new_verb_list = [verb for verb in verbs if not verb.endswith('s')]

# method 3
new_verb_list = list(filter(lambda verb: not verb.endswith('s'), verbs))


# filtering and then mapping
new_verb_list = [verb+'s' for verb in verbs if not verb.endswith('s')]
print (new_verb_list)