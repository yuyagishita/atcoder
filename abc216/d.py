n, m = map(int, input().split())

a = [[] for _ in range(m)]

# ontop[x]: 色xのうち一番上にあるボールの、その筒の集合
ontop = [[] for _ in range(n+1)]

stack = []

for i in range(m):
    k = int(input())
    a[i] = list(map(int, input().split()))[::-1]
    color = a[i][-1]
    ontop[color].append(i)
    if len(ontop[color]) == 2:
        stack.append(color)

done_cnt = 0

while len(stack) != 0:
    color = stack.pop()
    done_cnt += 1
    x, y = ontop[color]
    a[x].pop()
    if len(a[x]) != 0:
        new_color = a[x][-1]
        ontop[new_color].append(x)
        if len(ontop[new_color]) == 2:
            stack.append(new_color)
    a[y].pop()
    if len(a[y]) != 0:
        new_color = a[y][-1]
        ontop[new_color].append(y)
        if len(ontop[new_color]) == 2:
            stack.append(new_color)

if done_cnt == n:
    print('Yes')
else:
    print('No')
