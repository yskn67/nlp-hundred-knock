#! /usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    f = open('hightemp.txt', 'r')
    cnt = 0
    for line in f:
        cnt += 1
    print("wc -l: ", cnt)
    f.close()


if __name__ == '__main__':
    main()
