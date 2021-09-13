n = int(input())
a = list(map(int, input().split()))
ans = sorted(a)
print(a.index(ans[-2])+1)
