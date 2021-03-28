from bisect import bisect

N = int(input())
c = [[int(_) for _ in input().split()] for i in range(N)]
l = []

for i in range(len(c)):
    i = c[i][0]
    i = int(i)
    n = bisect(l, i)
    if n < len(l):
        l[n] = i
    else:
        l += i,

print(N-len(l))
