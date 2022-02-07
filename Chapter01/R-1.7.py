# R-1.7 Give a single command that computes the sum from Exercise R-1.6, rely-
# ing on Python’s comprehension syntax and the built-in sum function.


def SumOddSqure(data: int) -> int:
    return sum(i * i for i in range(data) if i % 2 != 0)


for t in range(10, 20):
    print(SumOddSqure(t))
