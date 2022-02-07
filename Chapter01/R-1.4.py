# R-1.4 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.
from math import sqrt
from math import ceil


def RootSum(data: int) -> int:
    sum = 0
    for i in range(data):
        sum += i * i
    return sum


for t in range(10, 20):
    print(RootSum(t))
