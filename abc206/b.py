n = int(input())

ans = 0
total = 0

i = 1
while True:
    total += i
    ans += 1

    if total >= n:
        print(ans)
        exit()

    i += 1
