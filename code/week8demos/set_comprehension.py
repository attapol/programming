#!/usr/bin/env python3
# -*- coding: utf-8 -*-


nouns = ['buildings', 'building', 'pool', 'tree','pools']

plural_noun_set = set()
for noun in nouns:
    if not noun.endswith('s'):
        plural_noun_set.add(noun + 's')
    else:
        plural_noun_set.add(noun)


print(plural_noun_set)