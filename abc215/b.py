n = int(input())

k = 0
while True:
    if 2**k <= n:
        k += 1
        continue
    else:
        break

print(k-1)
