def solve(n, children, xxx):
    dp = [-1] * n
    q = [0]
    while q:
        v = q[-1]

        if dp[v] == -1:
            q.extend(children[v])
            dp[v] = -2
            continue

        q.pop()
        can = 1
        mask = (1 << xxx[v] + 1) - 1
        total = 0
        for u in children[v]:
            can = ((can << xxx[u]) | (can << dp[u])) & mask
            total += xxx[u] + dp[u]
        if can == 0:
            return False
        dp[v] = total - (can.bit_length() - 1)
    return True


n = int(input())
children = [set() for _ in range(n)]
for i, p in enumerate(map(int, input().split()), start=1):
    children[p - 1].add(i)
xxx = list(map(int, input().split()))

print('POSSIBLE' if solve(n, children, xxx) else 'IMPOSSIBLE')
