from random import randint
n = 5
matrix = [[randint(0,100)for i in range(n)]for j in range(n)]
print(matrix)
max_value = float('-inf')
for row in matrix:
	for value in row:
		if value > max_value:
			max_value = value
print(max_value)