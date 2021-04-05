P = 10**9 + 7

# 分割数をdpで求めておく
part = [[0]*(100 + 1) for _ in range(1000 + 1)]
part[0][0] = 1
for s in range(1000 + 1):
   for n in range(1, 100 + 1):
       if s >= n:
           part[s][n] = (part[s][n - 1] + part[s - n][n]) % P
       else:
           part[s][n] = part[s][n - 1]

# 入力
N, M = map(int, input().split())
killA = [int(x) for x in input().split()]
killB = [int(x) for x in input().split()]
totA, totB = sum(killA), sum(killB)

# キル数でグループ分けしておく
# グループの数などが後で必要
sepA, sepB = [], []
sizeA, sizeB = 1, 1
for i in range(1, N):
   if killA[i] == killA[i - 1]:
       sizeA += 1
   else:
       sepA.append(sizeA)
       sizeA = 1
for i in range(1, M):
   if killB[i] == killB[i - 1]:
       sizeB += 1
   else:
       sepB.append(sizeB)
       sizeB = 1
sepA.append(sizeA)
sepB.append(sizeB)
nA, nB = len(sepA), len(sepB)

# dpA[i][j] は
# i番目までの同キル数グループの総デス数がj
# の時のあり得るデス数の組み合わせの数
dpA = [[0]*(totB + 1) for _ in range(nA)]
for i in range(nA):
   if i == 0:
       for j in range(totB + 1):
           dpA[i][j] = part[j][sepA[i]]
       continue
   for j in range(totB + 1):
       for k in range(j + 1):
           dpA[i][j] = (dpA[i][j] + part[k][sepA[i]] * dpA[i - 1][j - k]) % P
ansA = dpA[nA - 1][totB]

# dpB も同じ
dpB = [[0]*(totA + 1) for _ in range(nB)]
for i in range(nB):
   if i == 0:
       for j in range(totA + 1):
           dpB[i][j] = part[j][sepB[i]]
       continue
   for j in range(totA + 1):
       for k in range(j + 1):
           dpB[i][j] = (dpB[i][j] + part[k][sepB[i]] * dpB[i - 1][j - k]) % P
ansB = dpB[nB - 1][totA]
ans = ansA * ansB % P

# 出力
print(ans)
