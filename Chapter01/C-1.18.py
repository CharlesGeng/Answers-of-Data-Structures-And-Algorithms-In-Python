# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

def generator(data: int) -> list[int]:
    return list(d * (d+1) for d in data)


data = list(range(10))
print(generator(data))
