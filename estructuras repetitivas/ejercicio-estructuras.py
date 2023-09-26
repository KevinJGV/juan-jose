#ejercicio 1
numero = int(input("ingrese el numero a verifcar: "))

m = 1

total = 0

while(m<numero):
    if numero%m == 0:
        total = total + m
    m += 1

if total == numero:
    print("perfecto")
else:
    print("no es perfecto")

#ejercicio 2

matricula = float(input("valor de la matricula: "))

import math

matricula_Base = 10000  
aumento = 0.07    

años = math.log(2) / math.log(1 + aumento)

print(f"La matrícula se duplicará en {años:.1f} años.")

#ejercicio 3

import random

total_puntos = 1000000

numero_de_hits = 0


for i in range(total_puntos):
   
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    distance = x**2 + y**2

   
    if distance <= 1:
        numero_de_hits += 1


estimado_pi = 4 * numero_de_hits / total_puntos

print(f"Estimación de π usando {total_puntos} puntos aleatorios: {estimado_pi}")
