#EJEMPLO 1 - Hacer un progrma auq ewyuade a un profe con las notas de estudiantres.
# El profesor ingresa la nota de los 10 estudiantes que tiene y el programa le muestra
# el promedio de las notas, la nota mayor, la nota menor y las tres primeras notas de 
# mayor a menor.

def LeerFloat(msg):
    while True:
        try:
            n = float(input(msg))
            if n >= 0 and n<=5.0:
                return n
            else:
                print("Error. Nota no válida")
                input("Digite cualquier tecla para continuar...")
        except ValueError:
            print("Error! Ingrese un numero entero valido")

notMen = -1
notMay = 6
promNotas = 0.0
lstNotas = []
Mejores = []

for i in range (1,11):
    Nota = LeerFloat(f"Ingrese nota del estudiante #{i}: ")
    lstNotas.append(Nota)

notMen = min(lstNotas)
print("La nota menor es: ", notMen)
notMay = max(lstNotas)
print("La nota mayor es: ", notMay)
promNotas = sum(lstNotas) / 10
print(f"El promedio de las notas es: {promNotas:.2f}", )
lstNotas.sort(reverse=True)
print("Las tres mejores notas son: ")
print("\t1 -> ", lstNotas[0], "\n\t2 -> ",lstNotas[1], "\n\t3 -> ", lstNotas[2])