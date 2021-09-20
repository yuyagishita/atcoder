# t = int(input())
# case = [[int(_) for _ in input().split()] for i in range(t)]
#
# for i in range(len(case)):
#     ans = 0
#     while True:
#         if case[i][1] >= 1 and case[i][2] >= 1:
#             ans += 1
#             case[i][1] -= 1
#             case[i][2] -= 1
#         elif case[i][1] >= 1 and case[i][0] >= 2:
#             ans += 1
#             case[i][1] -= 1
#             case[i][0] -= 2
#         elif case[i][2] >= 2 and case[i][0] >= 1:
#             ans += 1
#             case[i][2] -= 2
#             case[i][0] -= 1
#         elif case[i][2] >= 1 and case[i][0] >= 3:
#             ans += 1
#             case[i][2] -= 1
#             case[i][0] -= 3
#         elif case[i][0] >= 5:
#             ans += 1
#             case[i][0] -= 5
#         else:
#             break
#
#     print(ans)

def solve(N2, N3, N4):
    N1, N2, N3 = N2, N4, N3//2
    ANS = 0

    comb = [(0, 1, 1), (2, 0, 1), (1, 2, 0), (3, 1, 0), (5, 0, 0)]
    for a, b, c in comb:
        k = N1 + N2 + N3
        if a > 0:
            k = min(k, N1//a)
        if b > 0:
            k = min(k, N2//b)
        if c > 0:
            k = min(k, N3//c)
        ANS += k
        N1 -= a * k
        N2 -= b * k
        N3 -= c * k

    print(ANS)


T = int(input())
for _ in range(T):
    solve(*map(int, input().split()))
