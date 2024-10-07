def get_matrix(size_of, amount, value):
    if size_of <= 0:
        return []
    elif amount <= 0:
        return []
    elif value <= 0:
        return []
    else:
        matrix = [[value] * amount] * size_of
        return matrix


matrix1 = get_matrix(2, 2, 10)
matrix2 = get_matrix(3, 5, 42)
matrix3 = get_matrix(4, 2, 13)
matrix4 = get_matrix(10, -1, 100)
matrix5 = get_matrix(-1, 10, 100)
matrix6 = get_matrix(-1000, -1000, 1000)
matrix7 = get_matrix(0, 0, 1000)
print(matrix1)
print(matrix2)
print(matrix3)
print(matrix4)
print(matrix5)
print(matrix6)
print(matrix7)