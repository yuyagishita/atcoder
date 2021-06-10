x, y = map(int, input().split())
janken = [0, 1, 2]
if x == y:
    print(x)
else:
    janken.remove(x)
    janken.remove(y)
    print(janken[0])
