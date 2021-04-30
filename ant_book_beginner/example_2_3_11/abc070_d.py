import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def dfs(v, p, d):
    '''現在の頂点 v, v の親 p, 現在の距離 d'''
    dist[v] = d
    # 頂点vとつながっている点を探索
    for u, c in graph[v]:  # u:つながっている頂点、c:距離
        # 最終地点は、親としかつながっていないのでdfs関数で深い階層へ探索しない
        if (u == p):
            continue
        # つながっている箇所を子に、現在の子を親にして、深い階層へと探索していく、距離は親のk地点までの距離とuからv
        dfs(u, v, d + c)

N = int(input())
graph = [[] for _ in range(N)]
dist = [0] * N

for i in range(N-1):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))

Q, K = map(int, input().split())
dfs(K-1, -1, 0)  # 頂点 K から全ての頂点への最短経路を前計算
for i in range(Q):
    x, y = map(int, input().split())
    print(dist[x-1] + dist[y-1])
