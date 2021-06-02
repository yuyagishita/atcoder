N, K = map(int, input().split())

ans = N
for i in range(K):
    a = [x for x in list(str(ans))]
    # g(x)は大きい順に並び替える
    g1 = int(''.join(sorted(a, reverse=True)))
    g2 = int(''.join(sorted(a)))
    f = g1-g2
    ans = f
print(ans)
