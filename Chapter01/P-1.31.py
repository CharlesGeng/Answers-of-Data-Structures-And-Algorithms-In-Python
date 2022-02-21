# Write a Python program that can “make change.” Your program should
# take two numbers as input, one that is a monetary amount charged and the
# other that is a monetary amount given. It should then return the number
# of each kind of bill and coin to give back as change for the difference
# between the amount given and the amount charged. The values assigned
# to the bills and coins can be based on the monetary system of any current
# or former government. Try to design your program so that it returns as
# few bills and coins as possible.


def make_change(charged, given, denominations=[10000, 5000, 2000, 1000, 500, 100, 50, 5, 1]) -> map:
    changes = {}
    change_total = given - charged
    for d in denominations:
        div, mod = divmod(change_total, d)
        if div:
            changes[d] = int(div)
            change_total = mod
    return changes


print(make_change(3532, 10000))
