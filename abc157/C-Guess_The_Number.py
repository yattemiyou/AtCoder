N, M = map(int, input().split())

number = ['0'] * N
if N > 1:
    number[0] = '1'

flag = [False] * N

answer = '-1'

for _ in range(M):
    s, c = input().split()

    index = int(s) - 1

    if N > 1 and index == 0 and c == '0':
        break

    if flag[index] and number[index] != c:
        break

    number[index] = c
    flag[index] = True
else:
    answer = ''.join(number)

print(answer)
