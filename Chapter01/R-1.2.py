from random import randint


def is_even(k) -> bool:
    return k & 1 == 0


# Test
for i in range(10):
    n = randint(10, 100)
    print(str.format('n={0}, result={1}', n, is_even(n)))
