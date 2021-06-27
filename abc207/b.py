a, b, c, d = map(int, input().split())

# 達成できない時はb>cの時
if b >= c*d:
    print('-1')
    exit()

x = a
y = 0
cnt = 0

while True:
    if x <= y*d:
        print(cnt)
        exit()
    x += b
    y += c
    cnt += 1
