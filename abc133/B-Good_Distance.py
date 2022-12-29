import math

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]


def is_good_distance(y, z):
    sum = 0

    for i in range(D):
        sum += (y[i] - z[i]) * (y[i] - z[i])

    n = int(math.sqrt(sum))

    if n * n == sum:
        return 1

    return 0


count = 0

for i in range(N):
    for j in range(i+1, N):
        count += is_good_distance(X[i], X[j])

print(count)
