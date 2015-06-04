########################################################################
# 03. 円周率                                                           #
#"Now I need a drink. alcoholic of course. after the heavy lectures    #
# involving quantum mechanics."という文を単語に分解し，                #
# 各単語の（アルファベット）文字数を先頭から出現順に並べたリストを     #
# 作成せよ                                                             #
########################################################################

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import collections

_str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

word_count = collections.defaultdict(int)

for i in range(0, len(_str)-1):
	char = _str[i]
	word_count[char] += 1

for k, v in sorted(word_count.items(), key=lambda x:x[1], reverse=True):
	print(k, v)

