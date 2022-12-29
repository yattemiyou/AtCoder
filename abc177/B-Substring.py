S = input()
T = input()

answer = len(T)

for i in range(len(S) - len(T) + 1):
    s = S[i:i+len(T)]

    d = sum([s[i] != T[i] for i in range(len(T))])

    if d < answer:
        answer = d

        if answer == 0:
            break

print(answer)
