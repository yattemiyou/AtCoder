N = int(input())
S = input()
T = input()

distance = bin(int(S, 2) ^ int(T, 2))[2:].count('1')

if distance % 2 == 1:
    print('-1')
    exit()

U = [''] * N

count = {'S': distance // 2, 'T': distance // 2}

for i in range(N):
    if S[i] == T[i]:
        U[i] = '0'
        continue

    if count['S'] > 0 and count['T'] > 0:
        U[i] = '0'

        c = 'S' if S[i] == '1' else 'T'
        count[c] -= 1
    elif count['S'] == 0:
        U[i] = S[i]
    else:
        U[i] = T[i]

print(*U, sep='')
