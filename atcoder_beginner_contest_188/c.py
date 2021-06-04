N = int(input())
A = list(map(int, input().split()))

hanbun = len(A)//2
left_a = A[:hanbun]
right_a = A[hanbun:]
mla = max(left_a)
mra = max(right_a)
if mla > mra:
    print(A.index(mra)+1)
else:
    print(A.index(mla)+1)
