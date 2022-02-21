# Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once.


def permutations(iterable):
    pool = tuple(iterable)
    n = len(pool)
    indices = list(range(n))   # 0,1,2,3,4,5
    cycles = list(range(n, 0, -1))  # 6,5,4,3,2,1
    yield tuple(pool[i] for i in indices[:n])
    while n:
        for i in reversed(range(n)):
            cycles[i] -= 1
            print(i)
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:n])
                break
        else:
            return


for s in permutations('catdog'):
    print(''.join(s))
