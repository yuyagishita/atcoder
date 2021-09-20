# この問題はBit全探索じゃない。計算量を考えると時間オーバーする。
# ans = 0
# for i in range(2**len(s)):
#     hantei = ['c', 'h', 'o', 'k', 'u', 'd', 'a', 'i']
#     for j in range(len(s)):
#         if ((i >> j) & 1):
#             if s[j] == hantei[0]:
#                 hantei.pop(0)
#
#     if len(hantei) == 0:
#         ans += 1
#
#
# print(ans)

# dpで配列を１次元にする方法
# s = input()
# chokudai = ' chokudai'
# mod = 10**9 + 7
# dp = [0] * 9
# dp[0] = 1
#
# for c in s:
#     for i in range(9):
#         if chokudai[i] == c:
#             dp[i] += dp[i-1]
#             dp[i] %= mod
#
# print(dp[-1])

# dpで配列を2次元にする方法
s = input()
mod = 10**9 + 7
t = 'chokudai'
# dp = [[1 if i == 0 else 0 for _ in range(9)] for i in range(len(s)+1)]
dp = [[0 for _ in range(9)] for i in range(len(s)+1)]

for i in range(len(s) + 1):
    dp[i][0] = 1

for i in range(len(s)):
    for j in range(8):
        if s[i] != t[j]:
            dp[i+1][j+1] = dp[i][j+1]
        else:
            dp[i+1][j+1] = (dp[i][j+1] + dp[i][j]) % mod

print(dp[len(s)][8])
