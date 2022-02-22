# Write a Python program that simulates a handheld calculator. Your pro-
# gram should process input from the Python console representing buttons
# that are “pushed,” and then output the contents of the screen after each op-
# eration is performed. Minimally, your calculator should be able to process
# the basic arithmetic operations and a reset/clear operation.

operators = "+-*/"


def calculator() -> float:
    formular = []
    while True:
        txt = input()
        if txt:
            if txt == 'reset' or txt == 'clear':
                formular.clear()
            else:
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
