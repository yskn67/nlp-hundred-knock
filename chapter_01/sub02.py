#! /usr/bin/env python
# -*- coding: utf-8 -*-

_str1 = 'パトカー'
_str2 = 'タクシー'
merged_str = ''
for (bf, af) in zip(list(_str1), list(_str2)):
    merged_str = merged_str + bf + af
print(merged_str)
