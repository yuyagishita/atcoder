B = [tuple(map(int, input().split())) for _ in range(2)]
C = [tuple(map(int, input().split())) for _ in range(3)]

M = [[-1] * 3 for _ in range(3)]
def score():
    res = [0, 0]
    for i in range(3):
        for j in range(3):
            if i < 2:
                t = 0 if M[i][j] == M[i + 1][j] else 1
                res[t] += B[i][j]
            if j < 2:
                t = 0 if M[i][j] == M[i][j + 1] else 1
                res[t] += C[i][j]
    return res

def predict(t):
    if t == 9:
        return score()
    turn = t & 1
    res = [-1, -1]
    for i in range(3):
        for j in range(3):
            if M[i][j] >= 0: continue
            M[i][j] = turn
            tmp = predict(t + 1)
            M[i][j] = -1
            if res[turn] < tmp[turn]:
                res = tmp
    return res

ans = predict(0)
for s in ans:
    print(s)
