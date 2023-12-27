import random

# generate a 9x9 matrix with a number from 0 to 9x9
def generate_matrix():
    matrix = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append(i*9+j)
        matrix.append(row)
    return matrix

# shuffle the matrix
def shuffle_matrix(matrix):
    for i in range(9):
        for j in range(9):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            matrix[i][j], matrix[row][col] = matrix[row][col], matrix[i][j]

matrix = generate_matrix()
shuffle_matrix(matrix)

for i in range(9):
    for j in range(9):
        print(matrix[i][j], end=', ')
    print()