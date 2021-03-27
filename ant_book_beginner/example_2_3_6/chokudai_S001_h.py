from bisect import bisect

l = []
for i in [*open(0)][1].split():
    i = int(i)
    n = bisect(l, i)
    if n < len(l):
        l[n] = i
    else:
        l += i,
print(len(l))
