from tokenize import Double


def norm(v: list[int], p=2) -> Double:
    sum = 0
    for d in v:
        sum += d**p
    return sum ** (1/p)


print(norm([4, 4], 3))
