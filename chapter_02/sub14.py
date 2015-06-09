#-----------------------------------------------------------------------
# 14.先頭からN行を出力
#    自然数Nをコマンドライン引数などの手段で受け取り，
#    入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
#-----------------------------------------------------------------------

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
argv = sys.argv
argc = len(argv)

def main():
	f = open('hightemp.txt', 'r')
	for i, line in enumerate(f):
		if i >= int(argv[1]):
			break
		line = line.rstrip()
		print(line)

	f.close()

if __name__ == '__main__':
	main()
