H, W = map(int, input().split())

answer = 0

for _ in range(H):
    answer += input().count('#')

print(answer)
