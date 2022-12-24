N = int(input())
S = input()

for c in S:
    index = (ord(c) - ord('A') + N) % 26
    print(chr(ord('A') + index), end='')

print()
