a, b = map(int, input().split())

min_a = 1 * a
max_a = 6 * a

if min_a <= b <= max_a:
    print('Yes')
else:
    print('No')
