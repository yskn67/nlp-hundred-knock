#! /usr/bin/env python
# -*- coding: utf-8 -*-

import collections

_str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

word_count = collections.defaultdict(int)

for i in range(0, len(_str) - 1):
    char = _str[i]
    word_count[char] += 1

for k, v in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
    print(k, v)
