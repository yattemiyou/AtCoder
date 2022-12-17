s = ''.join(chr(ord('A') + i) for i in range(26))

K = int(input())

print(s[:K])
