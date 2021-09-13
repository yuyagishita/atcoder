n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

tmp = [0, 0]

for i in range(n):
    if i == 0:
        tmp[0] = a[i]
        tmp[1] = b[i]
        continue
    if a[i] <= tmp[1] and tmp[0] <= b[i]:
        if tmp[0] < a[i]:
            tmp[0] = a[i]
        if tmp[1] > b[i]:
            tmp[1] = b[i]
    else:
        print(0)
        exit(0)

ans = 0
for i in range(tmp[0], tmp[1]+1):
    ans += 1

print(ans)
