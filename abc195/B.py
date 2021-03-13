A, B, W = map(int, input().split())

W *= 1000
mi = float('inf')
ma = -1

for n in range(1000001):
    if A*n <= W and W <= B*n:
        mi = min(mi, n)
        ma = max(ma, n)

if mi == float('inf'):
    print('UNSATISFIABLE')
else:
    print(mi, ma)
