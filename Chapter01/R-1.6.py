# R-1.6 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def SumOddSqure(data: int) -> int:
    result = 0
    for i in range(data):
        if i % 2 == 1:
            result += i * i
    return result


for t in range(10, 20):
    print(SumOddSqure(t))
