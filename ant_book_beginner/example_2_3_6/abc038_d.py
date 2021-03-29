from bisect import bisect_left
from operator import itemgetter

n = int(input())
box = [list(map(int, input().split())) for i in range(n)]
# h_i は昇順にした上で、h_i が等しい場合 w_i は降順にソートする
box = sorted(box, key=itemgetter(0), reverse=True)  # w_i
box = sorted(box, key=itemgetter(1))  # h_i
dp = [float("inf")] * n
for i in range(n):
    dp[bisect_left(dp, box[i][0])] = box[i][0]
print(bisect_left(dp, float("inf")))
