#-----------------------------------------------------------------------
# 17.１列目の文字列の異なり
#    1列目の文字列の種類（異なる文字列の集合）を求めよ．
#    確認にはsort, uniqコマンドを用いよ．
#-----------------------------------------------------------------------

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main():
	f = open('hightemp.txt', 'r')
	prefecture = {}
	for line in f:
		words = line.split("\t")
		prefecture[words[0]] = 1
	f.close()

	for pref in prefecture.keys():
		print(pref)

if __name__ == '__main__':
	main()
