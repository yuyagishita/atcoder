x = input()
ans = 'Strong'
if x[0] == x[1] == x[2] == x[3]:
    ans = 'Weak'

tmp = 0
hantei = False
for i in range(len(x)):
    if i == 0:
        tmp = int(x[i])
        continue
    if tmp+1 == int(x[i]) or (tmp == 9 and int(x[i]) == 0):
        hantei = True
    else:
        hantei = False
        break

    tmp = int(x[i])

if hantei:
    ans = 'Weak'

print(ans)
