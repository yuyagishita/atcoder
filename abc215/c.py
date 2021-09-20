import itertools

s, k = map(str, input().split())

all_list = sorted(set(itertools.permutations(s)))

for i, v in enumerate(all_list):
    if i+1 == int(k):
        print(''.join(v))
        exit()
