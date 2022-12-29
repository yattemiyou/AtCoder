N = int(input())
L = list(map(int, input().split()))

answer = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if L[i] == L[j] or L[i] == L[k] or L[j] == L[k]:
                continue
            if L[i] + L[j] <= L[k] or abs(L[i] - L[j]) >= L[k]:
                continue
            answer += 1

print(answer)
