H, W = map(int, input().split())

C = []

for i in range(H):
    C.append(input())

for j in range(W):
    count = 0

    for i in range(H):
        if C[i][j] == '#':
            count += 1

    print(count, end=' ')

print()
