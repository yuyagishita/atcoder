a, b = map(int, input().split())

A = ''
B = ''
for i in range(a):
    A += str(b)

for j in range(b):
    B += str(a)

if A > B:
    print(B)
else:
    print(A)
