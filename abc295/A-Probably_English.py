N = int(input())

word = ['and', 'not', 'that', 'the', 'you']

for s in input().split():
    if s in word:
        print('Yes')
        break
else:
    print('No')
