import math

A, B, C = map(int, input().split())

answer = math.ceil(A / C) * C

if answer <= B:
    print(answer)
else:
    print(-1)
