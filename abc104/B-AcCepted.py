def get_answer(S):
    if S[0] != 'A':
        return False

    if S[2:-1].count('C') != 1:
        return False

    if sum(map(str.isupper, S)) != 2:
        return False

    return True


print('AC' if get_answer(input()) else 'WA')
