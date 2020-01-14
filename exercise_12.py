"""
Question 12
Question:
Write a program, which will find all such numbers between 1000 and 3000
(both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""


def check(n):
    if n // 10 == 0:
        return n % 2 == 0
    else:
        if (n % 10) % 2 == 0:
            return check(n // 10)
        return False


print(','.join([str(n) for n in range(1000, 3001) if check(n)]))
