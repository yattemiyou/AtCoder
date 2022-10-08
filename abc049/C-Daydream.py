S = input()

end = len(S)

while end > 0:
    for w in ['dream', 'dreamer', 'erase', 'eraser']:
        if S.rfind(w, 0, end) == end - len(w):
            end = end - len(w)
            break
    else:
        print('NO')
        break
else:
    print('YES')
