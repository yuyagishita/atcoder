N, M, S = map(int, input().split())
N **= 2
M -= N
S -= N*(N-1)//2
S -= N
mod = 10**5
# dp[i][j][k] -> i番目の数まで見る。i番目に割り当てる数はj以下。合計はk。となるようなパターン数
#dp[i][j][k] = dp[i][j-1][k] + dp[i-1][j][k-j]
dp = [[0]*(S+1) for _ in range(M+1)]

for i in range(M+1):
    dp[i][0] = 1

for i in range(N):
    for j in range(1, M+1):
        for k in range(S, -1, -1):
            dp[j][k] = dp[j-1][k]
            if k-j >= 0:
                dp[j][k] += dp[j][k-j]
            dp[j][k] %= mod

print(dp[-1][-1])
