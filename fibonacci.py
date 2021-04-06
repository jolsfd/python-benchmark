#!/usr/bin/env python3
import time

cache = {}


def fibonacci(n):
    global cache
    if n in cache:
        return cache[n]

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = result
    return result


start = time.time()

for i in range(0, 1001):
    result = fibonacci(i)
    print(i, result)

finish = time.time()
duration = finish - start
print(f"Computed all 1000 in {duration} seconds")
