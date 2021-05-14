N = input()
N_rev = N[::-1]
count = 0

# 末尾の0を数える
for i in range(len(N_rev)):
    if N_rev[i] == '0':
        count += 1

# 回文判定をする。
for j in range(count+1):
    if j != 0:
        N = '0' + N
        N_rev = N_rev + '0'
    if N == N_rev:
        print('Yes')
        exit(0)

print('No')
