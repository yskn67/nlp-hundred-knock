#-----------------------------------------------------------------------
# 05.n-gram
#    与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
#    この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
#
#-----------------------------------------------------------------------

#! /usr/bin/env python
# -*- coding: utf-8 -*-

_str = 'I am an NLPer'

def char_ngram(str, n):
	ngram = []
	for idx in range(0, len(str)-n+1):
		ngram.append(str[idx:idx+n])
	return ngram

def word_ngram(str, n):
	ngram = []
	words = str.split(' ')
	for idx in range(0, len(words)-n+1):
		ngram.append(words[idx:idx+n])
	return ngram

def main():
	c_bigram = char_ngram(_str, 2)
	w_bigram = word_ngram(_str, 2)

	print('char bigram')
	for bigram in c_bigram:
		print("\t", bigram)
	print('word bigram')
	for bigram in w_bigram:
		print("\t", bigram)

if __name__ == '__main__':
	main()
	
