S = input()
T = input()


def get_answer():
    global S

    for i in range(len(S)):
        S = S[-1] + S[0:-1]

        if S == T:
            return True

    return False


print('Yes' if get_answer() else 'No')
