# 7. Sum Numbers in Matrix
def sum_matrix(m):
    sum = 0
    for row in m:
        for col in row:
            sum += col
    return sum


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sum_matrix(m))
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(sum_matrix(m))
m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
print(sum_matrix(m))


# 8. Matrix Bombing
def calculate_sum(m, x, y):
    rows = len(m)
    cols = len(m[0])
    sum = 0
    current_position_points = m[x][y]
    for l in range(x-1, x+2, 1):
        for k in range(y-1, y + 2, 1):
            if l >= 0 and l < rows and k >= 0 and k < cols:
                if not (l == x and k == y):
                    value_to_add = m[l][k] - current_position_points
                    if value_to_add < 0:
                        sum += m[l][k]
                    else:
                        sum += current_position_points
    return sum


def matrix_bombing_plan(m):
    rows = len(m)
    cols = len(m[0])
    result = {}
    for row in range(rows):
        for col in range(cols):
            tuple_key = (row, col)
            result[tuple_key] = sum_matrix(m) - calculate_sum(m, row, col)
    return result

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


print(matrix_bombing_plan(m))
