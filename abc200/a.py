N = int(input())

if N / 100 > N // 100:
    print(N//100 + 1)
else:
    print(N//100)
