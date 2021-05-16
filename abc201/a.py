A = [int(_) for _ in input().split()]

sort_a = sorted(A)

if sort_a[2] - sort_a[1] == sort_a[1] - sort_a[0]:
    print('Yes')
else:
    print('No')
