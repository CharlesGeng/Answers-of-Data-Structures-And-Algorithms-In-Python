from random import randint

# Solution


def is_multiple(n, m) -> bool:
    if not isinstance(n, (int)):
        raise TypeError("n must be an integer.")
    if not isinstance(m, (int)):
        raise TypeError("m must be an integer.")
    return n % m == 0


# Test
for i in range(10):
    n = randint(10, 100)
    m = randint(1, 10)
    print(str.format('n={0}, m={1}, result={2}', n, m, is_multiple(n, m)))

print(is_multiple(15.2, 7))
print(is_multiple(15, 7.2))
