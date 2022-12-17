import numpy as np

N, M = map(int, input().split())

S = []

for _ in range(N):
    S.append(np.array([c == 'o' for c in input()]))

answer = 0

for i in range(N):
    for j in range(i + 1, N):
        if all(S[i] | S[j]):
            answer += 1

print(answer)
