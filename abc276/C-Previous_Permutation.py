N = int(input())
P = list(map(int, input().split()))

for index in range(N-1, 0, -1):
    if P[index-1] > P[index]:
        index -= 1
        break

for i in range(N-1, index, -1):
    if P[i] < P[index]:
        P[i], P[index] = P[index], P[i]
        break

print(*P[:index+1], end=' ')
print(*P[-1:index:-1])
