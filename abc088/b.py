n = int(input())
a = list(map(int, input().split()))

alice = 0
bob = 0

a.sort(reverse=True)

for index, item in enumerate(a):
    if index % 2 == 0:
        alice += item
    else:
        bob += item

print(alice-bob)
