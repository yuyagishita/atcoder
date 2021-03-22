import sys
input = sys.stdin.readline

mod = 1000000007

n, m, q = map(int, input().split())
A = tuple(map(int, input().split()))
dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][0] = 1
for i, a in enumerate(A):
    dp[i+1][0] = dp[i][0]
    for j in range(1, a+1):
        dp[i+1][j] = dp[i+1][j-1] + dp[i][j]
        dp[i+1][j] %= mod
    for j in range(a+1, m+1):
        dp[i+1][j] = dp[i+1][j-1] - dp[i][j-a-1] + dp[i][j]
        dp[i+1][j] %= mod
dp = dp[n]
G = [[0]*(m+1) for _ in range(n)]
for i, a in enumerate(A):
    G[i][0] = dp[0]
    for j in range(1, a+1):
        G[i][j] = dp[j] - dp[j-1]
        G[i][j] %= mod
    for j in range(a+1, m+1):
        G[i][j] = dp[j] - dp[j-1] + G[i][j-a-1]
        G[i][j] %= mod
for _ in range(q):
    k, x = map(int, input().split())
    k -= 1
    ans = G[k][m-x]
    print(ans)
