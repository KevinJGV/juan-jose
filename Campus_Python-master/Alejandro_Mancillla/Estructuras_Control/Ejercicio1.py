Nombre = input("Ingrese el nombre del estudiante: ")
Calificacion = int(input("Ingrese la calificacion: "))

if Calificacion >= 0 and Calificacion <= 59:
    NotaLetra = "D"
elif Calificacion <= 79:
    NotaLetra = "C"
elif Calificacion <= 89:
    NotaLetra = "B"
else:
    NotaLetra = "A"

print("\n","-" * 30)
print('Estudiante: ',Nombre)
print("Nota Cuantitativa: ",Calificacion)
print("Nota Cualitativa: ",NotaLetra)
print("-" * 30, "\n")