N = int(input())
S = input()

for step in range(1, N):
    answer = 0
    for i in range(0, N-step):
        if S[i] == S[i+step]:
            break
        answer += 1
    print(answer)
