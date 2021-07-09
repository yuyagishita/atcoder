n, k, *a = map(int, open(0).read().split())
y = sorted(a)[k % n]
print(*(k//n+(x < y)for x in a))
