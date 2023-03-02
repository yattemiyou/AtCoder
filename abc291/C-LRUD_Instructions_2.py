N = int(input())
S = input()

x, y = 0, 0

route = set()
route.add((x, y))

for c in S:
    if c == 'R':
        x += 1
    elif c == 'L':
        x -= 1
    elif c == 'U':
        y += 1
    elif c == 'D':
        y -= 1

    if (x, y) in route:
        print('Yes')
        break
    route.add((x, y))
else:
    print('No')
