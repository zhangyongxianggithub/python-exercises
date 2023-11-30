"""
Question:
Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 * C * D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:

100,150,180
The output of the program should be:

18,22,24
"""
from math import *

numbers = input('input numbers comma-separated: ')
for i in numbers.split(','):
    print(round((float(i) * 50 * 2 / 30) ** 0.5), end=',')
print()
# this is my solution
# !/usr/bin/env python
# next is python2 solution
c = 50
h = 30
value = []
items = [x for x in input('input numbers comma-separated: ').split(',')]
for d in items:
    value.append(str(int(round(sqrt(2 * c * float(d) / h)))))
print(','.join(value))

C, H = 50, 30


def calc(D):
    return sqrt(2 * C * D / H)


D = input('inout numbers comma-separated: ').split(',')
D = [str(round(calc(int(i)))) for i in D]
print(','.join(D))
