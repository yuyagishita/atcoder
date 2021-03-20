from heapq import heappop, heappush

INF = 2 * 10**15

# 入力
N, M, X = map(int, input().split())
H = [0]
for _ in range(N):
    H.append(int(input()))
conn = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, T = map(int, input().split())
    if H[A] >= T:
        conn[A].append((B, T))
    if H[B] >= T:
        conn[B].append((A, T))

# ダイクストラ法でコストを計算
cost = [INF] * (N + 1)
cost[1] = 0
q = [(0, 1)]
while q:
    # c, x in q は x にコスト c で到達する行き方があるということ
    c, x = heappop(q)

    # コストの最小値を更新しない場合はスルー
    if cost[x] < c:
        continue

    # h == 木x に到達したときのフクロモモンガの高さ
    h = max(0, X - cost[x])
    for y, t in conn[x]:

        # 木を降りてから飛び移る場合
        if h - t > H[y]:
            tt = h - H[y]

        # そのまま飛び移る場合
        elif 0 <= h - t <= H[y]:
            tt = t

        # 木を登ってから飛び移る場合
        else:
            tt = 2 * t - h

        # cost[y] を更新
        if cost[y] > cost[x] + tt:
            cost[y] = cost[x] + tt
            heappush(q, (cost[y], y))

# 木N のテッペンまでいくのに必要なコストを計算
ans = H[N] + cost[N] - max(0, X - cost[N])

# 出力
print(ans if ans < INF else -1)
