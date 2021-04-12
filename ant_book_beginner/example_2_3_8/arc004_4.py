N,M = list(map(int,input().split()))
p = 10**9+7

flag = 1
if N<0:
    flag = -1
N = N*flag

pf={}
m=N
for i in range(2,int(m**0.5)+1):
    while m%i==0:
        pf[i]=pf.get(i,0)+1
        m//=i
if m>1:pf[m]=1

MAXN = 10**5+100
f = [1]
for i in range(MAXN):
    f.append(f[-1] * (i+1) % p)
def nCr(n, r, mod=p):
    return f[n] * pow(f[r], mod-2, mod) * pow(f[n-r], mod-2, mod) % mod

out = pow(2,M-1,p)
for v in pf.values():
    out = out * nCr(v+M-1,v,p)%p
print(out)
