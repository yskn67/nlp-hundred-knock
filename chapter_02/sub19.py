#! /usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    f = open('hightemp.txt', 'r')
    column = {}
    lines = []
    for line in f:
        line = line.rstrip()
        words = line.split("\t")
        lines.append(words)
        if column.get(words[0]) is None:
            column[words[0]] = 1
        else:
            column[words[0]] += 1
    f.close()
    sorted_lines = sorted(lines, key=lambda x: (column[x[0]], x[0]), reverse=True)

    for words in sorted_lines:
        line = "\t".join(words)
        print(line)


if __name__ == '__main__':
    main()
