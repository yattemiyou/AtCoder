N = int(input())

user = set()

for i in range(N):
    S = input()

    if not S in user:
        print(i + 1)
    user.add(S)
