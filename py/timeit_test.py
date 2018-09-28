import random
import timeit
import heapq
import time

MIN_VAL = -10000000
MAX_VAL = 10000000
N = 10000000#100000000
M = 10
loop = 10


def main1():
    a = [random.randrange(start=MIN_VAL, stop=MAX_VAL) for _ in range(N)]
    b = sorted(a)[:M]


def main2():
    a = [random.randrange(start=MIN_VAL, stop=MAX_VAL) for _ in range(N)]
    b = heapq.nsmallest(M, a, key=None)
    time.sleep(50)

main2()

result = timeit.timeit('main()', number=loop)
print(result)