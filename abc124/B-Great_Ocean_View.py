N = int(input())
H = list(map(int, input().split()))

max = H[0]
answer = 1

for i in range(1, N):
    if H[i] >= max:
        max = H[i]
        answer += 1

print(answer)
