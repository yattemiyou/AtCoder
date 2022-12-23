S = input()

if S[0] != 'A' or S[2:-1].count('C') != 1:
    print('WA')
else:
    index = S.find('C')

    if S[1:index].islower() and S[index+1:].islower():
        print('AC')
    else:
        print('WA')
