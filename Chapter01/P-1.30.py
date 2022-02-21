# Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.


def counter(d: int) -> (int):
    result = 0
    while d >= 2:
        result += 1
        d /= 2
    return result


print(counter(1024))
