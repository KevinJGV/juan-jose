# #ciclo para
# for m in range(10): 
#      print(m, end=", ")

# # ******
# *    *
# *    *
# *    *
# ****** 
 
for m in range(6):
    print("*", end="")

print("")

for m in range(3):
    print("*    *")
    
for m in range(6):
    print("*", end="")
    
piramide = int(input("Elija el tamaño de la piramide"))

for m in range(piramide):
    print((1+ m) * "*")
    

#capturar las notas de un curso y calcular el promedio de estas
# mostrar en pantalla el resultado del promedio

cant = int(input("cantidad de notas: "))
sumaNotas = 0
for m in range(1, cant + 1):
    nota = float(input(f"ingrese la nota #{m}: "))
    sumaNotas = sumaNotas + nota
    
prom = sumaNotas / cant

print(f"el promedio de las notas es: {prom:.1f}")
