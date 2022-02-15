# Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.

def myReverse(data: list) -> list:
    return data[::-1]


data = list(range(10))

print(myReverse(data))
print(data)
data.reverse()
print(data)
