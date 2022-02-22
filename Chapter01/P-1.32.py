# Write a Python program that can simulate a simple calculator, using the
# console as the exclusive input and output device. That is, each input to the
# calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
# can be done on a separate line. After each such input, you should output
# to the Python console what would be displayed on your calculator.

from ast import Num


operators = "+-*/"


def calculator() -> float:
    formular = []
    while True:
        txt = input()
        if txt:
            formular.append(txt)
        else:
            break
    temp = 0
    while len(formular) > 2:
        d = formular[1]
        if d == "+":
            temp = int(formular[0]) + int(formular[2])
        elif d == '-':
            temp = int(formular[0]) - int(formular[2])
        elif d == '*':
            temp = int(formular[0]) * int(formular[2])
        elif d == '/':
            temp = int(formular[0]) / int(formular[2])
        else:
            break
        formular = formular[3:]
        formular.insert(0, temp)
    return formular[0]


result = calculator()
print(result)
