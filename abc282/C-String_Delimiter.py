N = int(input())
S = input()

is_replace = True

for c in S:
    if c == '"':
        is_replace = not is_replace
    elif c == ',' and is_replace:
        c = '.'

    print(c, end='')

print()
