H, W = map(int, input().split())

compression = [True] * W

a = []
for i in range(H):
    row = input()
    if row == '.' * W:
        continue
    a.append(row)

    for j in range(W):
        if row[j] == '#':
            compression[j] = False

for i in range(len(a)):
    for j in range(W):
        if compression[j]:
            continue
        print(a[i][j], end='')
    print()
