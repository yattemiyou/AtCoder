def base8_to_base9(base8):
    base10 = int(base8, 8)

    base9 = []

    while base10 > 0:
        base9.append(str(base10 % 9))

        base10 = base10 // 9

    return (''.join(base9[::-1])).replace('8', '5')


N, K = input().split()

if N == '0':
    print(0)
else:
    for i in range(int(K)):
        N = base8_to_base9(N)

    print(N)
