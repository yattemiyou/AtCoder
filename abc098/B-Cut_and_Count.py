N = int(input())
S = input()

answer = 0

for i in range(N-1):
    X = {c for c in S[:i+1]}
    Y = {c for c in S[i+1:]}

    n = len(X.intersection(Y))

    if n > answer:
        answer = n

print(answer)
