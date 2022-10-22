A, B = map(int, input().split())

answer = 0

for i in range(A, B + 1):
    if str(i)[0:2] == str(i)[-1:-3:-1]:
        answer += 1

print(answer)
