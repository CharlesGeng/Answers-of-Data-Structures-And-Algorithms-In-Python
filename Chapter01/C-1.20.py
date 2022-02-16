# Python’s random module includes a function shuffle(data) that accepts a
# list of elements and randomly reorders the elements so that each possi-
# ble order occurs with equal probability. The random module includes a
# more basic function randint(a, b) that returns a uniformly random integer
# from a to b (including both endpoints). Using only the randint function,
# implement your own version of the shuffle function.

from random import randint


def shuffle(data: list[int]) -> list[int]:
    ll = len(data)
    for i in range(ll):
        j = randint(0, ll-1)
        data[i], data[j] = data[j], data[i]
    return data


data = list(range(20))

print(shuffle(data))
