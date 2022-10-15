X, K = map(int, input().split())

answer = X

for i in range(1, K + 1):
    quotient = answer // 10
    carry = 1 if answer % 10 >= 5 else 0

    answer = quotient + carry

print(answer * 10 ** K)
