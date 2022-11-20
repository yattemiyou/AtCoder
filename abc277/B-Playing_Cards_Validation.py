N = int(input())

cards = set()
answer = True

for _ in range(N):
    S = input()

    if not answer:
        continue

    if S in cards:
        answer = False
        continue

    cards.add(S)

    if not S[0] in 'HDCS':
        answer = False
        continue

    if not S[1] in 'A23456789TJQK':
        answer = False
        continue

print('Yes' if answer else 'No')
