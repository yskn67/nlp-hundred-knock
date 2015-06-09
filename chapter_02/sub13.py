#-----------------------------------------------------------------------
# 13.col1.txtとcol2.txtをマージ
#    12で作ったcol1.txtとcol2.txtを結合し，
#    元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
#    確認にはpasteコマンドを用いよ．
#-----------------------------------------------------------------------

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main():
	in1 = open('col1.txt', 'r')
	in2 = open('col2.txt', 'r')
	for l1, l2 in zip(in1, in2):
		l1 = l1.rstrip()
		l2 = l2.rstrip()
		print(l1, "\t", l2)

	in1.close()
	in2.close()

if __name__ == '__main__':
	main()
