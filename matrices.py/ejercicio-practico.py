#ejercicio practico yt
rows = int(input("cuantas filas tendra la matrix?: "))
columns = int(input("cuantas columnas tendra la matrix?: "))

matrix = []
for row_position in range(rows):
    row = []
    for element in range(columns):
        row.append(int(input(f"introduce un elemento a la  fila {row_position}:")))
    matrix.append(row)

for row in matrix:
    print(row)