N = int(input())
li = list(map(int, input().split()))
rems = [0] * 200
 
for i in li:
    rem = i % 200
    rems[rem] += 1

ans = 0
 
for i in rems:
    ans += i * (i - 1) / 2
print(int(ans))
