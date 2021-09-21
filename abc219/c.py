x = input()
d = dict()

for i in range(26):
    nxt = chr(i + ord('a'))
    d[x[i]] = nxt

n = int(input())
ans = []

for _ in range(n):
    s = input()
    t = ''
    for char in s:
        t += d[char]

    ans.append((t, s))

ans.sort()

for i in range(n):
    print(ans[i][1])
