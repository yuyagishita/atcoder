n = int(input())

a = []
b = []
t = 0
ans = 0
for i in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

    t += x / y

# 火がぶつかる時間tは全体の半分
t /= 2

for i in range(n):
    ans += min(a[i], t * b[i])
    t -= min(a[i] / b[i], t)

print(ans)
