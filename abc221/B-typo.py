S = input()
T = input()


def get_answer():
    if S == T:
        return True

    i = 0
    while i < len(S) - 1:
        if S[i] != T[i]:
            if S[i] != T[i+1] or T[i] != S[i+1]:
                return False

            if S[i+2:] == T[i+2:]:
                return True
            else:
                return False
        i += 1

    return False


print('Yes' if get_answer() else 'No')
