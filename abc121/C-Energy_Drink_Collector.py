N, M = map(int, input().split())

store = []

for _ in range(N):
    store.append(tuple(map(int, input().split())))

money = 0

for s in sorted(store):
    n = min(s[1], M)

    M -= n
    money += n * s[0]

    if M <= 0:
        break

print(money)
