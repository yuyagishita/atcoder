n = int(input())

ed = int(1.08 * n)

if ed < 206:
    print('Yay!')
elif ed == 206:
    print('so-so')
else:
    print(':(')
