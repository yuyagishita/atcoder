n = int(input())
a = [int(_) for _ in input().split()]
ans = 0

for i in range(n):
    tmp = a[i] - 10
    if tmp > 0:
        ans += tmp

print(ans)
