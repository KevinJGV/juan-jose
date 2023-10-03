# Ejercicio
#hacer un programa que lea N estudiantes ( nombre y nota).  y nos mueste el promedio de la clase, el estudiante con menor nota y el estudiante con mayor nota.

def leerInt(msj):
    while True:
        try:
            n = int(input(msj))
            if n < 1:
                print("Nota invalido. debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar la nota")

def leerNombre(msj):
    while True:
        try:
            nom = input(msj)
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def leerNota(msj):
    while True:
        try:
            n = float(input(msj))
            if n < 0:
                print("Nota invalida. debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar la nota")  




n = leerInt("Cuantos estudiantes son? ")
lstNombres = []
lstNotas = []
for i in range(1, n+1):
    print("\nDatos del estudiante #:", i)
    lstNombres.append(leerNombre("Nombre? "))
    lstNotas.append(leerNota("Nota? "))

#Calcular y mostrar el promedio
prom = sum(lstNotas) / n
print("\n", "=" * 30)
print(f"El promedio del curso es: {prom:.1f}")

# Encontrar y mostrar el estudiante con la mayor nota
notaMayor = max(lstNotas)
posEstMayor = lstNotas.index(notaMayor)
nomEstMayoNota = lstNombres[posEstMayor]
print("El estudiante", nomEstMayoNota, " tiene la mayor nota:", notaMayor )

#encontrar estudiante con nota menor
notaMenor = min(lstNotas)
posEstMenor = lstNotas.index(notaMenor)
nomEstMenoNota = lstNombres[posEstMenor]
print("El estudiante", nomEstMenoNota, " tiene la menor nota:", notaMenor )