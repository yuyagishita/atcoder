N = int(input())
S = []
for i in range(N):
    tmp = input()
    S.append(tmp)

S_unique = list(set(S))
print(len(S_unique))
