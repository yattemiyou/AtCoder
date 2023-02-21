a = [0] * 3
b = [0] * 3
c = []

for _ in range(3):
    c.append(list(map(int, input().split())))


def solve():
    for a1 in range(0, 101):
        a[0] = a1
        b[0] = c[0][0] - a1
        b[1] = c[0][1] - a1
        b[2] = c[0][2] - a1

        for i in range(1, 3):
            a[i] = c[i][0] - b[0]
            for j in range(1, 3):
                if c[i][j] != a[i] + b[j]:
                    return 'No'
        return 'Yes'


print(solve())
