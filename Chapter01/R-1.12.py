# Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module in-
# cludes a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.

from random import randrange


def choice(data: list) -> int:
    return randrange(data[0], data[-1] + 1)


data = range(10)

for i in range(30):
    print(choice(data))
