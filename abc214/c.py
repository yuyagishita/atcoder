n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

min_i = 0

for i in range(n):
    if t[i] < t[min_i]:
        min_i = i

now_t = t[min_i]
ans = [0] * n
for i in range(n):
    now_i = (min_i + i) % n
    now_t = min(now_t, t[now_i])
    ans[now_i] = now_t
    now_t += s[now_i]

print(*ans)
