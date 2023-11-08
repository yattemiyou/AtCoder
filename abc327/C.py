A = [list(map(int, input().split())) for _ in range(9)]

def is_valid(i):
	row_numbers = set()
	column_numbers = set()
	block_numbers = set()

	for j in range(9):
		row_numbers.add(A[i][j])
		column_numbers.add(A[j][i])

		x = (j//3)+(i//3)*3
		y = (j%3)+(i%3)*3
		block_numbers.add(A[x][y])

	return len(row_numbers) == 9 and len(column_numbers) == 9 and len(block_numbers) == 9

for i in range(9):
	if not is_valid(i):
		print('No')
		break
else:
	print('Yes')
