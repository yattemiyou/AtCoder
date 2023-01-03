import math

A, B, C, X, Y = map(int, input().split())

answer = math.inf

for i in range(0, max(X, Y) + 1):
    price = max(X-i, 0)*A + max(Y-i, 0)*B + 2*i*C

    if price < answer:
        answer = price

print(answer)
