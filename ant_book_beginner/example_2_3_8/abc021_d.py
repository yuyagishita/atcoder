N = int(input())
K = int(input())


def inv(n, MOD=10**9+7):  # MODを法とした逆元
    return pow(n, MOD-2, MOD)


def comb(n, r, MOD=10**9+7, mx=10**6):  # mx:求めておきたい階乗の最大値
    fact = [1] * (mx+1)  # 階乗を格納するリスト
    for i in range(mx):
        fact[i+1] = fact[i] * (i+1) % MOD  # 階乗を計算
    return (fact[n] * inv(fact[n-r]) * inv(fact[r])) % MOD


ans = comb(N+K-1, K)
print(ans)
