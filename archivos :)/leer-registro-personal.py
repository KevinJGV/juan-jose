def llenar_matriz (mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            mat [f][c] = "-----"
        #print (" ")

def print_matrices (mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print (mat[f][c], end = "\t\t")
        print (" ")

archivo = open("archivos :)/datos-Empleado.dat", "r")

mat_informacion = []

for linea in archivo:
    lista_linea = []
    lista_linea.append(linea.split(","))
    mat_informacion.append(lista_linea)





archivo.close()

for i in range(1,len(mat_informacion)):
    print ("\n", "-" * 40)
    print (f"ID: {mat_informacion[i][0][0]}")
    print (f"NOMBRE: {mat_informacion[i][0][1]}")
    print (f"EDAD: {mat_informacion[i][0][2]}")
    print (f"SEXO: {mat_informacion[i][0][3]}")
    print (f"TELÉFONO: {mat_informacion[i][0][4]}")
    print ("-" * 40)
#print_matrices (mat_informacion)
