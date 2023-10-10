matrix_a = [[1,2,3],
           [4,5,6],
           [7,8,9]]

matrix_b = [[9,8,7],
           [6,5,4],
           [3,2,1]]

matrix_c = []
for row in range(len(matrix_a)):
    new_row = []
    for column in range(len(matrix_a[0])):
        new_row.append(matrix_a[row][column] + matrix_b[row][column])
    matrix_c.append(new_row) 
    
for row in range(len(matrix_a)):
    if row != 1:
        print(f"{matrix_a[row]}  {matrix_b[row]} {matrix_a[row]}")
    else:
        print(f"{matrix_a[row]}  + {matrix_b[row]} =  {matrix_a[row]}")
    