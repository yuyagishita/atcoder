from math import sqrt

n = int(input())
xy = [list(map(int, input().split())) for i in range(n)]

xy = sorted(xy)


def f(xy1, xy2):
    a = xy2[0] - xy1[0]
    b = xy2[1] - xy1[1]
    return sqrt(a*a + b*b)


ans = 0
for i in range(n):
    for j in range(i, n):
        tmp = f(xy[i], xy[j])
        if ans < tmp:
            ans = tmp

print(ans)
