n = int(input())
s = list(input())
q = int(input())
is_flipped = 0

for _ in range(q):
    t, a, b = map(int, input().split())

    if t == 2:
        is_flipped ^= 1
        continue

    a -= 1
    b -= 1
    if is_flipped:
        a = (a + n) % (2 * n)
        b = (b + n) % (2 * n)
    s[a], s[b] = s[b], s[a]

if is_flipped:
    s = s[n:] + s[:n]

print(''.join(s))
