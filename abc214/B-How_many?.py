S, T = map(int, input().split())

answer = 0

for a in range(101):
    for b in range(101):
        for c in range(101):
            if a + b + c <= S and a * b * c <= T:
                answer += 1

print(answer)
