from sys import stdin
def input(): return stdin.readline()[:-1]


prime_table = [True] * 2*10**6
cumsum = [0] * len(prime_table)

count = 0

for i in range(2, len(prime_table)):
    if prime_table[i]:
        for j in range(2*i, len(prime_table), i):
            prime_table[j] = False

        if i != 2 and prime_table[(i+1)//2]:
            count += 1
    cumsum[i] = count

Q = int(input())

for _ in range(Q):
    l, r = map(int, input().split())
    print(cumsum[r] - cumsum[l-1])
