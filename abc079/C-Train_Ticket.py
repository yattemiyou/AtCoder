A, B, C, D = input()

op = ['-', '+']

for i in range(8):
    formula = A + op[i & 0x04 != 0]
    formula += B + op[i & 0x02 != 0]
    formula += C + op[i & 0x01 != 0]
    formula += D

    if eval(formula) == 7:
        print(formula + '=7')
        break
