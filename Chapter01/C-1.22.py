# Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is, it returns
# an array c of length n such that c[i] = a[i]·b[i], for i = 0,...,n−1.

def dot_product(a: list[int], b: list[int]) -> list[int]:
    c = []
    for i in range(len(a)):
        c.append(a[i] * b[i])

    return c


a = list(range(10))
b = list(range(10, 20))

print(dot_product(a, b))
