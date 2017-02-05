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
    sorted_lines = sorted(lines, key=lambda x: float(x[2]), reverse=True)

    for words in sorted_lines:
        line = "\t".join(words)
        print(line)


if __name__ == '__main__':
    main()
