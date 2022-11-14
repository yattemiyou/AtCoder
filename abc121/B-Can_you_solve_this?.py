N, M, C = map(int, input().split())
B = list(map(int, input().split()))

answer = 0

for _ in range(N):
    A = list(map(int, input().split()))

    sum = 0

    for i in range(M):
        sum += A[i] * B[i]

    if sum + C > 0:
        answer += 1

print(answer)
