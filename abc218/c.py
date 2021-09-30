from typing import Tuple


n = int(input())

s = [list(input()) for _ in range(n)]
t = [list(input()) for _ in range(n)]


def rotate(s):
    res = [[''] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = s[j][n-1-i]
    return res


def is_same(s, t):
    s_min_i = n
    s_min_j = n
    t_min_i = n
    t_min_j = n

    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                s_min_i = min(s_min_i, i)
                s_min_j = min(s_min_j, j)
            if t[i][j] == '#':
                t_min_i = min(t_min_i, i)
                t_min_j = min(t_min_j, j)

    ok = True
    for i in range(n):
        for j in range(n):
            si = s_min_i + i
            sj = s_min_j + j
            if si < n and sj < n:
                schar = s[si][sj]
            else:
                schar = '.'
            ti = t_min_i + i
            tj = t_min_j + j
            if ti < n and tj < n:
                tchar = t[ti][tj]
            else:
                tchar = '.'

            if schar != tchar:
                ok = False

    return ok


ok = False
ok |= is_same(s, t)
s = rotate(s)
ok |= is_same(s, t)
s = rotate(s)
ok |= is_same(s, t)
s = rotate(s)
ok |= is_same(s, t)
s = rotate(s)

if ok:
    print('Yes')
else:
    print('No')
