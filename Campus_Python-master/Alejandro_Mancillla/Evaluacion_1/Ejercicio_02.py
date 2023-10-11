#AREA DE UN TRIANGULO
import math
print("CALCULAR AREA DE UN TRIANGULO\n")

#DATOS DE ENTRADA
a = float(input("Ingrese la medida del primer lado: "))
b = float(input("Ingrese la medida del segundo lado: "))
c = float(input("Ingrese la medida del tercer lado: "))

#PROCESO
p = (a + b + c)/2
if p > a and p > b and p > c:
    Area = math.sqrt(p * (p - a) * (p - b)* (p - c))
    print(f"El Area del Triangulo es = {Area:.02f}")
else:
    print("Las medidas ingresadas no corresponden a un triangulo")