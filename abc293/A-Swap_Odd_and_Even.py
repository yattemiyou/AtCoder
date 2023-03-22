S = input()

for i in range(len(S)//2):
    print(S[i*2+1], S[i*2], sep='', end='')
print()
