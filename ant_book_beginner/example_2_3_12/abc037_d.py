h, w = map(int, input().split())
xy = [[*map(int, input().split())] for _ in range(h)]
chk = [[None]*w for _ in range(h)]
mod = 10**9+7


def dfs(y, x):
    if chk[y][x] is not None:
        return chk[y][x]
    res = 1
    for ty, tx in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        ty += y
        tx += x
        if 0 <= ty < h and 0 <= tx < w and xy[y][x] > xy[ty][tx]:
            res += dfs(ty, tx) % mod
    chk[y][x] = res
    return chk[y][x]


ans = 0
for y in range(h):
    for x in range(w):
        ans += dfs(y, x)

print(ans % mod)
