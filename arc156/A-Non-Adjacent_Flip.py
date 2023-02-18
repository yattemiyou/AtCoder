answer = []


def solve():
    N = int(input())
    S = input()

    head = S.count('1')

    if head % 2 == 1:
        answer.append(-1)
    elif head == 2 and S.count('11') == 1:
        if N == 3:
            answer.append('-1')
        elif S == "0110":
            answer.append('3')
        else:
            answer.append('2')
    else:
        answer.append(head // 2)


T = int(input())

for _ in range(T):
    solve()

print(*answer, sep='\n')
