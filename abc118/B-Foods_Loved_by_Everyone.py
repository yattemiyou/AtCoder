N, M = map(int, input().split())

bucket = [0] * M

for _ in range(N):
    K, *A = map(int, input().split())

    for i in A:
        bucket[i-1] += 1

answer = 0

for i in bucket:
    if i == N:
        answer += 1

print(answer)
