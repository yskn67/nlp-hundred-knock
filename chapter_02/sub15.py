#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
argv = sys.argv
argc = len(argv)


def main():
    f = open('hightemp.txt', 'r')
    lines = []
    for line in f:
        line = line.rstrip()
        lines.append(line)
    f.close()

    n = int(argv[1])

    for i in range(-1 * n, 0):
        print(lines[i])


if __name__ == '__main__':
    main()
