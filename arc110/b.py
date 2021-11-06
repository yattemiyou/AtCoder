pattern = '110'
repetition = 10**10

def is_contain(t):
    head = t[0:len(pattern)]

    if head not in ['110', '101', '011']:
        return False

    t = t + head[len(t)%len(pattern):len(pattern)]

    return t.replace(head, '') == ''

n = int(input())
t = input()

count = pattern.count(t)

if count != 0:
    print(repetition * count)
    exit()

if t == '01':
    t = '011'

if not is_contain(t):
    print(0)
    exit()

count = t.count('0')

if t[-1] == '0':
    print(repetition - count + 1)
else:
    print(repetition - count)
