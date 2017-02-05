#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re

_cipher_num = 219


def get_cipher_char(char):
    cipher_char = chr(_cipher_num - ord(char))
    return cipher_char


def cipher(str):
    char_list = []
    for i in range(0, len(str)):
        idx_char = str[i]
        if re.match(r"[a-z]", idx_char):
            idx_char = get_cipher_char(idx_char)
        char_list.append(idx_char)
    cipher_str = ''.join(char_list)
    return cipher_str


def main():
    str = "I am a NLPer"
    print("original str:")
    print("\t", str)
    str = cipher(str)
    print("encrypt str:")
    print("\t", str)
    str = cipher(str)
    print("decrypt str:")
    print("\t", str)


if __name__ == '__main__':
    main()
