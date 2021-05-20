N, K = map(int, input().split())

for i in range(K):
    if N % 200 == 0:
        N //= 200
    else:
        tmp = str(N) 
        tmp += '200'
        N = int(tmp)

print(N)
