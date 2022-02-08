n, q = map(int, input().split())
a = list(map(int, input().split()))
xk = [list(map(int, input().split())) for _ in range(q)]

# 配列を作る。要素数に合わせて
#d = dict.fromkeys(a, list())
#print(d)
value = [0]
d = {i: list(value) for i in a}

# ここで辞書の中に何番目にあるかの配列を作る。
for i in range(n):
    d[a[i]].append(i+1)

for i in range(q):
    x = xk[i][0]
    k = xk[i][1]
    if x in d and len(d[x]) > k:
        print(d[x][k])
    else:
        print(-1)
    
