N, X = map(int, input().split())
L = list(map(int, input().split()))

D = 0

for i in range(len(L)):
    D += L[i]

    if D > X:
        break

print(i + 1)
