N = int(input())

not_called = set(range(1, N+1))
called = set()

for i, n in enumerate(input().split()):
    n = int(n)
    if not i+1 in called:
        not_called.discard(n)
        called.add(n)

print(len(not_called))
print(*not_called)
