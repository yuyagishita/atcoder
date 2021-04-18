n, z ,w = map(int, input().split())
a = [int(_) for _ in input().split()]

ans = max(abs(a[n-1]-w), abs(a[n-2]-a[n-1]))
print(ans)

# 別解
# n,*a=map(int,open(0).read().split())
# print(max(abs(a[n+1]-a[1]),abs(a[n]-a[n+1])))
