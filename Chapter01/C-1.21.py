# Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).

user_input = []

while True:
    try:
        user_input.insert(0, input())
    except EOFError:
        break

for l in user_input:
    print(l)
