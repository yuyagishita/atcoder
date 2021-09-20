s = [input() for _ in range(4)]

ans_list = ['H', '2B', '3B', 'HR']

for i in ans_list:
    if i in s:
        s.remove(i)

if len(s) == 0:
    print('Yes')
else:
    print('No')
