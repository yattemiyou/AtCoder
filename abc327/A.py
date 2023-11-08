N = int(input())
S = input()

print('Yes' if S.find('ab') >= 0 or S.find('ba') >= 0 else 'No')
