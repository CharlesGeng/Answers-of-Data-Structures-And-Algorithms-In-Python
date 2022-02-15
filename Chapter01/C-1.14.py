# Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.

def IsProductOdd(data: list) -> bool:
    return len(set(d for d in data if d % 2 == 1)) > 1


# One odd number, expect False
d1 = [2, 2, 31, 10, 410, 100, 2, 30, 230, 232]
# One odd numbers, expect True
d2 = [2, 2, 31, 11, 410, 100, 2, 30, 230, 232]

print(IsProductOdd(d1))
print(IsProductOdd(d2))
