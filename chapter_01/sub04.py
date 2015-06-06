#-----------------------------------------------------------------------
# 04.元素記号
#    "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations
#    Might Also Sign Peace Security Clause. Arthur King Can."という文を
#    単語に分解し、1,5,6,7,8,9,15,16,19番目の単語は先頭の1文字、それ以外
#    の単語は先頭に2文字を取り出し、取り出した文字列から単語の位置
#    （先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）
#    を作成せよ
#
#-----------------------------------------------------------------------

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re

_str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

words = _str.split(' ')
index = {}

for (cnt, word) in enumerate(words):
	cnt += 1
	word_index = _str.find(word)
	word_index += 1

	if( cnt in [1,5,6,7,8,9,15,16,19] ):
		key = word[:1] + ' '
	else:
		key = word[:2]
	index[key] = word_index

for k, v in sorted(index.items(), key=lambda x:x[1]):
	print( k, ": ", v )
