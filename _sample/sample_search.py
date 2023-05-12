N = int(input())
A = list(map(int, input().split()))
Q = int(input())
query = [int(input()) for _ in range(Q)]


def binary_search(a, value):
    left = 0
    right = len(a) - 1

    while left != right:
        middle = (left + right) // 2

        if a[left] > value:
            return str(a[left])
        if a[right] <= value:
            return 'not exist'
        if a[middle-1] <= value and a[middle] > value:
            return str(a[middle])

        if a[middle] > value:
            right = middle
        else:
            left = middle + 1

    if a[left] > value:
        return str(a[left])
    else:
        return 'not exist'


for v in query:
    print(binary_search(A, v))
