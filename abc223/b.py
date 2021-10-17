n = input()
max_n = n
min_n = n

for i in range(len(n)):
    if max_n < n:
        max_n = n

    if min_n > n:
        min_n = n

    n = n[1:len(n)] + n[0]

print(min_n)
print(max_n)
