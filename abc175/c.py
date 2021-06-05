X, K, D = map(int, input().split())


def sgn(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


if X > 0:
    x_greedy = X - K * D
else:
    x_greedy = X + K * D

if sgn(X) == sgn(x_greedy):
    print(abs(x_greedy))
    exit()

x_r = X % D
x_l = x_r - D

# * rにたどり着いたときの歩数の偶奇を求めている。
r_parity = (abs(X - x_r) // D) % 2

# * 原点に近いところでr, lを交互に繰り返して最後は偶奇でどっちにいるか判定できる。
if K % 2 == r_parity:
    print(abs(x_r))
else:
    print(abs(x_l))
