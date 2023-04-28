# -*- coding:utf-8 -*-
# @Date  : 2019/2/27

import sys


def test_for_sys(year, name, body):
    print('the year is', type(year))
    print('the name is', name)
    print('the body is', body)


if __name__ == '__main__':
    try:
        year, name, body = sys.argv[1:4]
        test_for_sys(year, name, body)
    except Exception as e:
        print(sys.argv)
        print(e)
