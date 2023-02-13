N, M = map(int, input().split())
a = list(map(int, input().split()))

stack = []

for i in range(1, N + 1):
    if i in a:
        stack.append(i)
    else:
        print(i, end=' ')
        if len(stack) > 0:
            print(*stack[::-1], end=' ')
            stack.clear()
print()
