# Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).

def is_distinct(data: list[int]) -> bool:
    return len(data) == len(set(data))


d1 = list(range(19))
d1.append(10)
d2 = list(range(20))

print(is_distinct(d1))
print(is_distinct(d2))
