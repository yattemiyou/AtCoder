S = input()

head = None
words = []

for i in range(len(S)):
    if S[i].isupper() and head == None:
        head = i
    elif S[i].isupper() and head != None:
        words.append(S[head:i+1])
        head = None

print(''.join(sorted(words, key=str.lower)))
