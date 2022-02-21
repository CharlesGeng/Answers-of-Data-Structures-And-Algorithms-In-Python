# Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once.


def permutations(iterable, ):
    pool = tuple(iterable)
    n = len(pool)
    r = n
    indices = list(range(n))   # 0,1,2,3,4,5
    cycles = list(range(n, n-r, -1))  # 5,4,3,2,1,0
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


for s in permutations('catdog'):
    print(''.join(s))
