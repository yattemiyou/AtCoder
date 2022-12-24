A, B = map(int, input().split())
S = input()


def get_answer():
    if len(S) != A + B + 1:
        return False
    if S[A] != '-':
        return False
    if sum(map(str.isdecimal, S)) != A + B:
        return False
    return True


print('Yes' if get_answer() else 'No')
