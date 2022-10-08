N, A, B = map(int, input().split())

s = 0

for n in range(1, N + 1):
    if A <= sum(map(int, str(n))) <= B:
        s = s + n

print(s)
