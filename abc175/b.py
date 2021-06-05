N = int(input())
L = list(map(int, input().split()))
ans = 0 

for i in range(N):
    for j in range(N):
        if i >= j or L[i] == L[j]:
            continue
        for k in range(N):
            if j >= k or L[j] == L[k] or L[k] == L[i]:
                continue
            if L[i] + L[j] > L[k] and  L[j] + L[k] > L[i] and L[k] + L[i] > L[j]:
                ans += 1

print(ans)
