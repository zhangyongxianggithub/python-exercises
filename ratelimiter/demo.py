import datetime
import string
import random

from ratelimiter import RateLimiter


@RateLimiter(max_calls=2, period=1)
def do_something():
    print(datetime.datetime.now(), '\n')


while True:
    print(datetime.datetime.now(), '\n')
    print(''.join(random.sample(string.ascii_letters + string.digits, 8)))
    do_something()
