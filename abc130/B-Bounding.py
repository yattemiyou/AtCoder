N, X = map(int, input().split())
L = list(map(int, input().split()))

D = 0

for i in range(N):
    D += L[i]

    if D > X:
        break
else:
    i += 1

print(i + 1)
