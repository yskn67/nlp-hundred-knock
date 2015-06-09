#-----------------------------------------------------------------------
# 16.ファイルをN分割する
#    自然数Nをコマンドライン引数などの手段で受け取り，
#    入力のファイルを行単位でN分割せよ．
#    同様の処理をsplitコマンドで実現せよ．
#-----------------------------------------------------------------------

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
argv = sys.argv
argc = len(argv)

def main():
	n     = int(argv[1])
	fname = 1
	cnt   = 0
	words = []
	f = open('hightemp.txt', 'r')
	for line in f:
		words.append(line)
	f.close()

	out = open('out'+str(fname)+'.txt', 'w')
	for idx in range(0, len(words)):
		out.write(words[idx])
		cnt += 1
		if cnt >= n:
			fname += 1
			cnt = 0
			out.close()
			if idx != len(words)-1:
				out = open('out'+str(fname)+'.txt', 'w')

if __name__ == '__main__':
	main()
