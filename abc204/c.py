import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
done = [False] * n
edge = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)


def dfs(v):
    if done[v]:
        return
    done[v] = True
    for to in edge[v]:
        dfs(to)


ans = 0
for s in range(n):
    for i in range(n):
        done[i] = False
    dfs(s)
    ans += sum(done)

print(ans)
