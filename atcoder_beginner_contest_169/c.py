a, b = map(str, input().split())

a = int(a)
b, c = map(int, b.split('.'))
ans = a * (b * 100 + c)//100

print(ans)
