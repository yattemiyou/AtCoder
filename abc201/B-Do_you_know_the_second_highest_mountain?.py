N = int(input())

mountains = []

for _ in range(N):
    S, T = input().split()

    mountains.append([int(T), S])

print(sorted(mountains, reverse=True)[1][1])
