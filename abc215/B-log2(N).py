N = int(input())

answer = 0

while N != 1:
    N = N >> 1
    answer += 1

print(answer)
