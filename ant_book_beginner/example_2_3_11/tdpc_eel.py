n, k = map(int, input().split())
edge = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)
M = 10**9 + 7


def dfs(p, par):
    dp = [[1, 0, 0]]
    for c in edge[p]:
        if c == par:
            continue
        a = dfs(c, p)
        nex = [[0] * 3 for i in range(min(k + 1, len(dp) + len(a) - 1))]
        for i in range(len(dp)):
            for j in range(3):
                for l in range(min(len(a), k + 1 - i)):
                    for m in range(3 - j):
                        nex[i + l][j + m] = (nex[i + l]
                                             [j + m] + dp[i][j] * a[l][m]) % M
        dp = nex
    if len(dp) <= k:
        dp.append([0] * 3)
    for i in range(len(dp) - 1, -1, -1):
        dp[i][2] = 0
        dp[i][1] = (dp[i][0] + dp[i][1]) % M
        if i > 0:
            dp[i][0] = (dp[i][0] + dp[i - 1][1] + dp[i - 1][2]) % M
    return dp


print(dfs(0, -1)[k][0])
