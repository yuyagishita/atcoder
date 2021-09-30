p = list(map(int, input().split()))

ans = ''
for i in p:
    ans += chr(i+ord('a')-1)

print(ans)
