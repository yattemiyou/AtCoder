import math

X = int(input())

answer = 1

for b in range(2, int(math.sqrt(X)) + 1):
    p = 2
    while b ** p <= X:
        if b ** p > answer:
            answer = b ** p
        p += 1

print(answer)
