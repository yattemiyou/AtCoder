import bisect
from collections import defaultdict


###
def divide_character(s):
    d = defaultdict(list)

    for i, c in enumerate(s):
        d[c].append(i)

    return d


def find_character(d, c, start):
    """
    （注）start以上の範囲で検索する
    """
    if c not in d:
        return -1

    index = bisect.bisect_left(d[c], start)

    # 最後尾かどうか
    return d[c][index] if index < len(d[c]) else -1


def rfind_character(d, c, start):
    """
    （注）start未満の範囲で検索する
    """
    if c not in d:
        return -1

    index = bisect.bisect_left(d[c], start)

    # 最前列かどうか
    return d[c][index-1] if index > 0 else -1
###


###
def merge():
    A = [3, 14, 15, 92]
    B = [6, 53, 58]
    N = len(A)
    M = len(B)

    C = (N + M) * [0]

    i, j = 0, 0
    for index in range(N + M):
        if A[i] < B[j]:
            C[index] = A[i]
            i += 1

            if i >= N:
                C[index + 1:] = B[j:]
                break
        else:
            C[index] = B[j]
            j += 1

            if j >= M:
                C[index + 1:] = A[i:]
                break
    return C
###
