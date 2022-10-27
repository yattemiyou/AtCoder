import math

N, D = map(int, input().split())

answer = 0

for i in range(N):
    X, Y = map(int, input().split())

    if math.sqrt(X**2 + Y**2) <= D:
        answer += 1

print(answer)
