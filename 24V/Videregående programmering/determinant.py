matrix_size = input("Choose matrix size: ")
matrix = []
for i in range(int(matrix_size)):
    user_input = input(f"Enter {matrix_size} numbers for row {i+1}: ")
    matrix.append([int(j) for j in user_input.split(" ")])

test_matrix =[
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [1, 4, 5, 6, 7],
    [5, 4, 3, 2, -1],
    [1, 2, 1, 2, 1]
] # determinant = 8

def determinant(matrix) -> int:
    if len(matrix) == 1:
        return matrix[0][0]
    total = 0
    for i in range(len(matrix)):
        a = matrix[0][i]
        m = [line[:i] + line[i+1:] for line in matrix[1:]]
        total += (-1)**i * a * determinant(m)
    return total

print("Determinant:", determinant(matrix))