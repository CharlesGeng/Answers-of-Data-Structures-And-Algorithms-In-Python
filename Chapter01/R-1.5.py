# R-1.5 Give a single command that computes the sum from Exercise R-1.4, rely-
# ing on Python’s comprehension syntax and the built-in sum function.


def RootSum(data: int) -> int:
    return sum(i*i for i in range(data))


for t in range(10, 20):
    print(RootSum(t))
