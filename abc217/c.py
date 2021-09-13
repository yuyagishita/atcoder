n = int(input())
p = list(map(int, input().split()))

q = [[0] for i in range(n)]

for i in range(n):
    tmp = p[i]
    q[tmp-1][0] = i + 1

ans = ''
for i in q:
    ans += str(i[0]) + ' '

print(ans)
