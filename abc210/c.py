n, k = map(int, input().split())
c = list(map(int, input().split()))

# 配列でデータを持つとcが10^9を考えると重くなる。
# そこで辞書型を使う。
# tmp_list = []
ans = 0
tmp_list = dict()
now = 0

for i in range(n):
    if c[i] not in tmp_list.keys():
        tmp_list[c[i]] = 0

    if tmp_list[c[i]] == 0:
        now += 1
    tmp_list[c[i]] += 1
    if i >= k:
        tmp_list[c[i-k]] -= 1
        if tmp_list[c[i-k]] == 0:
            now -= 1
    ans = max(ans, now)

print(ans)
