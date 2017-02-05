#! /usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    f = open('hightemp.txt', 'r')
    out1 = open('col1.txt', 'w')
    out2 = open('col2.txt', 'w')
    for line in f:
        words = line.split("\t")
        out1.write(words[0])
        out1.write("\n")
        out2.write(words[1])
        out2.write("\n")
    out1.close()
    out2.close()
    f.close()


if __name__ == '__main__':
    main()
