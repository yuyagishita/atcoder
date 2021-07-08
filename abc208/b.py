from math import factorial

P = int(input())
answer = 0

for i in range(1, 11):
    divisor = factorial(i + 1)
    residue = P % divisor
    answer += residue // factorial(i)
    P -= residue

print(answer)
