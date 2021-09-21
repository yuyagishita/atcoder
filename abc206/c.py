import collections
from math import factorial

from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


n = int(input())
a = list(map(int, input().split()))

c = collections.Counter(a)

tyouhuku = 0
for k, v in c.items():
    if v > 1:
        # tyouhuku += factorial(v) / factorial(2) / factorial(v - 2)
        tyouhuku += cmb(v, 2)

# kumiawase = factorial(n) / factorial(2) / factorial(n - 2)
kumiawase = cmb(n, 2)

ans = kumiawase - tyouhuku

print(ans)
