#-----------------------------------------------------------------------
# 06.集合
#    "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
#    それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
#    さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
#-----------------------------------------------------------------------

#! /usr/bin/env python
# -*- coding: utf-8 -*-

_str1 = 'paraparaparadise'
_str2 = 'paragraph'

def char_ngram(str, n):
	ngram = []
	for idx in range(0, len(str)-n+1):
		ngram.append(str[idx:idx+n])
	return ngram

def main():
	X = set(char_ngram(_str1, 2))
	Y = set(char_ngram(_str2, 2))

	sum	= X | Y
	product	= X & Y
	diff	= X - Y

	print("SUM:")
	print("\t", sum)
	print("PRODUCT:")
	print("\t", product)
	print("DIFF:")
	print("\t", diff)


if __name__ == '__main__':
	main()
	
