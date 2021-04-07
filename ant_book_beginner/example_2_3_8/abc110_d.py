# 法
P = 10**9 + 7

# 繰り返し二乗法
def modpow(a, n):
   if n == 0:
       return 1
   if n % 2 == 0:
       return (modpow(a, n // 2)**2) % P
   else:
       return (a * modpow(a, n // 2)**2) % P
       
# mod P での逆元を求める関数
def inv(a):
   return modpow(a, P - 2)

# 階乗 mod P をあらかじめ計算しておく   
fac = [1]*(2*10**5)
for i in range(1, 2*10**5):
   fac[i] = (i * fac[i - 1]) % P

# エラトステネスの篩で素数を求める
primes = []
check = [False]*10**5
for p in range(2, 10**5):
   if check[p]:
       continue
   primes.append(p)
   for j in range((10**5 - 1) // p + 1):
       check[p * j] = True

# 素因数分解してくれる関数       
def pf(M):
   ans = {}
   for p in primes:
       e = 0
       while M % p == 0:
           M //= p
           e += 1
       if e > 0:
           ans[p] = e
   if M > 1:
       ans[M] = 1
   return ans
   
# 入力
N, M = map(int, input().split())

# M を素因数分解
pfM = pf(M)

# 重複組合せの積 mod P を計算
ans = 1
for p in pfM:
   e = pfM[p]
   dup = (fac[e + N - 1] * inv(fac[e]) * inv(fac[N - 1])) % P
   ans = (ans * dup) % P
   
# 出力
print(ans)
