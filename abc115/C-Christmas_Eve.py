N, K = map(int, input().split())
h = sorted([int(input()) for _ in range(N)])

min = 10 ** 9

for i in range(N - (K - 1)):
    if min > h[i + (K - 1)] - h[i]:
        min = h[i + (K - 1)] - h[i]

print(min)
