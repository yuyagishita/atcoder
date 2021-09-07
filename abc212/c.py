import numpy as np

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = float("inf")

for i in b:
    idx = np.abs(np.asarray(a) - i).argmin()
    tmp = np.abs(a[idx] - i)
    if ans > tmp:
        ans = tmp

print(ans)
