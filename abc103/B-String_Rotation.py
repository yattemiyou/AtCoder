S = input()
T = input()


def get_answer():
    for i in range(len(S)):
        if S[len(S)-i:] + S[0:len(S)-i] == T:
            return True

    return False


print('Yes' if get_answer() else 'No')
