A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
b = [int(input()) for _ in range(N)]

for i in range(3):
    for j in range(3):
        if A[i][j] in b:
            A[i][j] = '*'


def get_answer():
    for i in range(3):
        if A[i][0] == A[i][1] == A[i][2] == '*':
            return 'Yes'

    for j in range(3):
        if A[0][j] == A[1][j] == A[2][j] == '*':
            return 'Yes'

    if A[0][0] == A[1][1] == A[2][2] == '*':
        return 'Yes'

    if A[0][2] == A[1][1] == A[2][0] == '*':
        return 'Yes'

    return 'No'


print(get_answer())
