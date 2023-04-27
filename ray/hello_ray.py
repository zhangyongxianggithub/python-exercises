# -*- coding: utf-8 -*-
import datetime
import time
import ray


def sleep_method():
    time.sleep(1)
    print("i am sleeping")


if __name__ == "__main__":
    print("hello world")
    print(datetime.datetime.now())
    ray.init()
    context = ray.get_runtime_context()
    env = context.runtime_env
    print(str(env))
    fo = open("/home/ray/foo.txt", "a")
    fo.write(str(env))
    fo.flush()
    time.sleep(3333333)
