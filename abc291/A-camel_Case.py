import re

S = input()

m = re.search(r'[A-Z]', S)

print(m.start() + 1)
