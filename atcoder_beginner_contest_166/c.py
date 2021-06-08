n, m = map(int, input().split())
hs = list(map(int, input().split()))

edge = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

cnt = 0

for node in range(n):
    good = True
    for neighbor in edge[node]:
        if hs[node] <= hs[neighbor]:
            good = False
    if good:
        cnt += 1

print(cnt)
