from random import randint


def minmax(data):
    min_n, max_n = data[0], data[0]
    for i in data[1:]:
        if i < min_n:
            min_n = i
        elif i > max_n:
            max_n = i
    return (min_n, max_n)


test_data = []
for i in range(10):
    test_data.append(randint(10, 100))

print(test_data)
print(minmax(test_data))
