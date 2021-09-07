s = []
for i in range(3):
    s.append(input())

atcoder_list = ['ABC', 'ARC', 'AGC', 'AHC']

for i in s:
    atcoder_list.remove(i)

print(atcoder_list[0])
