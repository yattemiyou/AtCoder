import sys

N, M, X = map(int, input().split())
C = [0] * N
A = [[]] * N

for i in range(N):
    C[i], *A[i] = map(int, input().split())

answer = sys.maxsize

for pattern in range(2 ** N):
    sum = 0
    level = [0] * M

    for i in range(N):
        if (pattern & (1 << i)) == 0:
            continue

        sum += C[i]
        level = [level[j] + A[i][j] for j in range(M)]

        if all(level[j] >= X for j in range(M)):
            if sum < answer:
                answer = sum
            break

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
