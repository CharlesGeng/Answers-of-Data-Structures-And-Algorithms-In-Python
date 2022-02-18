# In Section 1.8, we provided three different implementations of a generator
# that computes factors of a given integer. The third of those implementa-
# tions, from page 41, was the most efficient, but we noted that it did not
# yield the factors in increasing order. Modify the generator so that it reports
# factors in increasing order, while maintaining its general performance ad-
# vantages.

from pkg_resources import yield_lines


def factor(data: int):
    k = 1
    temp = []
    while k*k < data:
        if data % k == 0:
            yield k
            temp.insert(0, data // k)
        k += 1
    if k*k == data:
        yield k
    for d in temp:
        yield d


for d in factor(210):
    print(d)
