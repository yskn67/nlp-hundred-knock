#-----------------------------------------------------------------------
# 18.各行を3コラム目の数値の降順にソート
#    各行を3コラム目の数値の逆順で整列せよ
#    （注意: 各行の内容は変更せずに並び替えよ）．
#    確認にはsortコマンドを用いよ
#    （この問題はコマンドで実行した時の結果と合わなくてもよい）．
#-----------------------------------------------------------------------

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main():
	f = open('hightemp.txt', 'r')
	lines = []
	for line in f:
		line = line.rstrip()
		words = line.split("\t")
		lines.append(words)
	f.close()
	sorted_line = sorted(lines, key=lambda x: float(x[2]), reverse = True)

	for words in lines:
		line = "\t".join(words)
		print(line)

if __name__ == '__main__':
	main()
