import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N-1)]
MOD = 10**9+7

es = [[] for _ in range(N)]
for a, b in AB:
    a, b = a-1, b-1
    es[a].append(b)
    es[b].append(a)

MAXN = N+5
fac = [1, 1] + [0]*MAXN
finv = [1, 1] + [0]*MAXN
inv = [0, 1] + [0]*MAXN
for i in range(2, MAXN+2):
    fac[i] = fac[i-1] * i % MOD
    inv[i] = -inv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i-1] * inv[i] % MOD


def dfs(v, p=-1):
    if p >= 0 and len(es[v]) == 1:
        return (1, 0)
    sz = 0
    cm = 1
    for to in es[v]:
        if to == p:
            continue
        c, s = dfs(to, v)
        sz += s+1
        cm *= c * finv[s+1]
        cm %= MOD
    cm *= fac[sz]
    cm %= MOD
    return (cm, sz)


ans = 0
for i in range(N):
    ans += dfs(i)[0]
    ans %= MOD
print((ans * inv[2]) % MOD)
