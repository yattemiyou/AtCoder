N = int(input())

count = sum([input() == 'For' for _ in range(N)])

print('Yes' if count > N // 2 else 'No')
