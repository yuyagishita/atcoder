import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m, l, x = map(int, input().split())
a = list(map(int, input().split()))
dp = [[99999]*m for _ in range(3)]
# dp[i][j]=燃料をi番目までみて休憩所jに止まるのに必要な最小の周回回数
for i in range(3):
    dp[i][0] = 0
# print(dp)
for i in range(n):
    for j in range(m):
        # print(i)
        dp[(i+1) % 3][(j+a[i]) % m] = min(dp[(i+1) % 3][(j+a[i]) % m], dp[i % 3][j]+a[i]/m)
        dp[(i+1) % 3][j] = min(dp[(i+1) % 3][j], dp[i % 3][j])
# for i in dp:
    # print(i)
print('Yes' if dp[n % 3][l] <= x else 'No')
