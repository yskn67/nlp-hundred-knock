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
