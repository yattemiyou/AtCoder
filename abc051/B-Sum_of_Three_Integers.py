K, S = map(int, input().split())

count = 0

for X in range(K + 1):
    for Y in range(K + 1):
        if 0 <= S - (X + Y) <= K:
            count = count + 1

print(str(count))
