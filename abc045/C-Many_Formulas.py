S = input()
n = len(S) - 1

answer = 0

for i in range(2**n):
    bits = bin(i)[2:].zfill(n)

    start = 0
    while (end := bits.find('1', start)) != -1:
        answer += int(S[start:end+1])
        start = end + 1

    answer += int(S[start:])

print(answer)
