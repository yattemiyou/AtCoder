S = input()

for i in range(1, len(S)):
    length = len(S) - i

    if length % 2 != 0:
        continue

    if S[0:length//2] == S[length//2:-1*i]:
        print(length)
        break
