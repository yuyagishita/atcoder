from bisect import bisect_left
INF = float('inf')

N = int(input())
L = []
for _ in range(N):
    x, r = map(int,input().split())
    L.append((x + r, x - r))
L.sort()

P = [INF] * (N + 1)
for i in range(N):
    P[bisect_left(P, - L[i][1])] = - L[i][1]
print(P.index(INF))
