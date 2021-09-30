n = int(input())

st = []
for i in range(n):
    tmp = input().split()
    st.append(tmp)

for i in range(n):
    for j in range(n):
        if i >= j:
            continue
        if st[i][0] == st[j][0] and st[i][1] == st[j][1]:
            print('Yes')
            exit()

print('No')
