number_Of_Matrix = int(input("¿cuantas matrices quieres sumar?: "))

if number_Of_Matrix > 1:
     
    rows = int(input("¿cuantas filas tendran las matrices?: "))
    columns = int(input("¿cuantas columnas tendran las matrices?: "))

    matrix_List = []

    #llenado de matrices
    for number in range(number_Of_Matrix):
        matrix = []
        for row in range(rows):
            new_row = []
            for column in range(columns):
                new_row.append(

                int(input(f"introduce un elemento para la matriz {number + 1} fila{row}, columna{column}: ")))
            matrix.append(new_row)
        matrix_List.append(matrix)

    #suma de las matricesf
    matrix = []
    for row in range(rows):
        new_row = []
        for column in range(columns):
            sum_matrix = 0
            for  matrix_position in range(len(matrix_List)):
                sum_matrix += matrix_List[matrix_position][row][column]
            new_row.append(sum_matrix)
        matrix.append(new_row)
    

else:
    print(" se necesitan dos  o mas matrices para realizar la suma.")