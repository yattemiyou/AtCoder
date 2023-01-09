import math

S = input()

answer = math.inf

for i in range(len(S) - 2):
    answer = min(abs(int(S[i:i+3]) - 753), answer)

print(answer)
