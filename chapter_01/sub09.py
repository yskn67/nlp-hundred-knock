#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

_str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
_enable_num = 4


def get_randomize_word(word):
    if len(word) <= _enable_num:
        return word

    first = word[0]
    last = word[-1]
    to_random = list(word[1:-1])

    random.shuffle(to_random)
    randomized_word = first + ''.join(to_random) + last
    return randomized_word


def get_randomize_str(str):
    words = str.split(' ')
    for idx in range(0, len(words)):
        words[idx] = get_randomize_word(words[idx])
    randomized_str = ' '.join(words)
    return randomized_str


def main():
    print("original str:")
    print("\t", _str)
    print()
    print("randomized str:")
    print("\t", get_randomize_str(_str))


if __name__ == '__main__':
    main()
