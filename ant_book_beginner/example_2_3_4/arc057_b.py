n, k = list(map(int, input().split()))
a = [int(input()) for _ in range(n)]

dp = [[float('inf')]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 0
dp[1][1] = 1

s = 0
for i in range(1, n):
    s += a[i-1]
    for j in range(n):
        dp[i+1][j+1] = min(dp[i][j+1], dp[i][j]+dp[i][j]*a[i]//s+1)

if s+a[n-1] == k:
    print(1)
else:
    for i in reversed(range(n+1)):
        if dp[n][i] <= k:
            print(i)
            break
