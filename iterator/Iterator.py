import datetime
import itertools

from datetime import date

cont = itertools.count()


class Num(object):
    def __iter__(self):
        return self

    def __next__(self) -> int:
        i = next(cont)
        if i > 10:
            raise StopIteration('reach ten')
        return i


if __name__ == '__main__':
    d = date.today()
    print(d.isoformat())
    n = Num()
    for i in n:
        print(i)
