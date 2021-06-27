# この問題は各区間を閉区間に直すことを考える。

n = int(input())
l = [0] * n
r = [0] * n
for i in range(n):
    t, l[i], r[i] = map(int, input().split())
    if t == 2:
        r[i] -= 0.5
    if t == 3:
        l[i] += 0.5
    if t == 4:
        l[i] += 0.5
        r[i] -= 0.5
ans = 0
for i in range(n):
    for j in range(i+1, n):
        ans += (max(l[i], l[j]) <= min(r[i], r[j]))
print(ans)
