def divide(n, b, e):
	if e == 0:
		return b if n == 1 else -1
	if n % b != 0:
		return -1
	return divide(n//b, b, e-1)

B = int(input())

for i in range(1, 18):
	if (result := divide(B, i, i)) > 0:
		print(result)
		break
else:
	print(-1)

