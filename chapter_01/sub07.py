#! /usr/bin/env python
# -*- coding: utf-8 -*-


def template(x, y, z):
    str = "{0}時の{1}は{2}".format(x, y, z)
    return str


def main():
    str = template(12, "気温", 22.4)
    print(str)


if __name__ == '__main__':
    main()
