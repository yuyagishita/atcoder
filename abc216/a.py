x, y = input().split('.')

if 0 <= int(y) <= 2:
    print(x+'-')
if 3 <= int(y) <= 6:
    print(x)
if 7 <= int(y) <= 9:
    print(x+'+')
