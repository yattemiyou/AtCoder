n = int(input())
p = list(map(int, input().split()))

operation = []

target = 1

while target <= n:
    if p[target - 1] == target:
        target = target + 1
        continue

    try:
        index = p.index(target, target - 1)
    except ValueError:
        print(-1)
        exit()

    for i in range(index - (target - 1)):
        p[index - 1 - i], p[index - i] = p[index - i], p[index - 1 - i]
        operation.append(index - i)

    target = index + 1

if len(operation) != n - 1:
    print(-1)
    exit()

if p != list(range(1, n + 1)):
    print(-1)
    exit()

for o in operation:
    print(o)
