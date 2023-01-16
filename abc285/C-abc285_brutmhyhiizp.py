S = input()

answer = 0

for c in S:
    answer *= 26
    answer += ord(c) - ord('A') + 1

print(answer)
