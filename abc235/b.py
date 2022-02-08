n = int(input())
h = list(map(int, input().split()))

ans = 0
for i in range(n):
    if ans < h[i]:
        ans = h[i]
    else:
        break
    

print(ans)
