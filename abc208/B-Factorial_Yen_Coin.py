coin = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

P = int(input())

answer = 0

for i in range(len(coin) - 1, -1, -1):
    n = P // coin[i]
    P -= coin[i] * n
    answer += n

print(answer)
