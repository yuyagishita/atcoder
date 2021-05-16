S = input()
ans = 0

for i in range(10000):
    T = str(i).zfill(4)
    ok = True
    for d in range(10):
        if S[d] == '?':
            continue
        if S[d] == 'o':
            if not str(d) in T:
                ok = False
        if S[d] == 'x':
            if str(d) in T:
                ok = False

    if ok:
        ans += 1

print(ans)
