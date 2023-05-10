import datetime

from ratelimiter import RateLimiter


@RateLimiter(max_calls=2, period=1)
def do_something():
    print(datetime.datetime.now(), '\n')


while True:
    do_something()
