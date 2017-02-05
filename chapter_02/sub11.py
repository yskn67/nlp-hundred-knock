#! /usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    f = open('hightemp.txt', 'r')
    for line in f:
        line = line.rstrip()
        line = line.replace("\t", " ")
        print(line)

    f.close()


if __name__ == '__main__':
    main()
