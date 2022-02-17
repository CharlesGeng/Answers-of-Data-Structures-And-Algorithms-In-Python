# Write a short program that takes as input three integers, a, b, and c, from
# the console and determines if they can be used in a correct arithmetic
# formula (in the given order), like “a+b = c,” “a = b−c,” or “a∗b = c.”

def arithmeti_check() -> str:
    a = int(input())
    b = int(input())
    c = int(input())
    if a + b == c:
        return "addition OK."
    elif a - b == c:
        return "Subtraction OK."
    elif a * b == c:
        return "Mutiplication OK"
    elif a//b == c:
        return "Division OK"
    else:
        return "Not suitble."


print(arithmeti_check())
