a, b, c = map(int, input().split())

# pow_ac = pow(a, c)
# pow_bc = pow(b, c)

# if pow_ac < pow_bc:
#     print('<')
# elif pow_ac > pow_bc:
#     print('>')
# else:
#     print('=')

if c % 2 == 0:
    a = abs(a)
    b = abs(b)

if a < b:
    print('<')
elif a > b:
    print('>')
else:
    print('=')
