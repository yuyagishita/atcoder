n = int(input())
a = list(map(int, input().split()))

for i in range(1, n+1):
    if i in a:
        a.remove(i)

if not a:
    print('Yes')
else:
    print('No')
