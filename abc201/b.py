N = int(input())
M = [[(_) for _ in input().split()] for i in range(N)]

for i in range(len(M)):
    M[i][1] = int(M[i][1])

sort_m = sorted(M, key=lambda x: (x[1]), reverse=True)

print(sort_m[1][0])
